import requests
from flask import Flask, session, abort, redirect, request, flash
import os, pathlib
from google.oauth2 import id_token
from pip._vendor import cachecontrol
from google_auth_oauthlib.flow import Flow
import google.auth.transport.requests 
from .secret import password,clientid

app=Flask("Google Login App")
app.secret_key=password

GOOGLE_CLIENT_ID=clientid


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1" 
#this is required for localhost as we currently dont have access to https secured network in our local host pc


client_secrets_file=os.path.join(pathlib.Path(__file__).parent,"/client_secret.json")

flow= Flow.from_client_secrets_file(
    client_secrets_file="client_secret.json",
    scopes=["https://www.googleapis.com/auth/userinfo.email","https://www.googleapis.com/auth/userinfo.profile", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return redirect("/login")
        return function(*args, **kwargs)
    return wrapper

@app.route('/login')
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

@app.route("/callback")
def callback():
   
    if "state" not in session or "state" not in request.args:
        return redirect("/login") 
    flow.fetch_token(authorization_response=request.url)
    if session["state"] != request.args["state"]:
        abort(500)
    credentials = flow.credentials
    cached_session = cachecontrol.CacheControl(requests.Session())
    token_request = google.auth.transport.requests.Request(session=cached_session)
    id_info = id_token.verify_oauth2_token(
        id_token=credentials.id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )
    session["google_id"] = id_info.get("sub")
    session["email"] = id_info.get("email")
    session["name"] = id_info.get("name")
    session["profile-picture"] = id_info.get("picture")
    flash("Login successful")
    return redirect('/protected_area')

    

@app.route('/logout')
def logout():
    session.pop("google_id", None)
    return redirect("/")

@app.route('/')
def index():
    return "Login using Google <a href='/login'><button>Login</button></a>"

@app.route('/protected_area')
@login_is_required
def protected_area():
    return "Logout <a href ='/logout'><button>Logout</button></a>"


if __name__=="__main__":
    app.run(debug=True)
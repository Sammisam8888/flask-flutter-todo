from application import app
from flask import render_template, request, redirect, url_for

@app.route('/')
def index():
    return render_template("layout.html", title="HomePage TODO App")
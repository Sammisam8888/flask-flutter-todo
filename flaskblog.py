from flask import Flask, render_template
app= Flask(__name__)

posts= [
    {
        'author' : 'John Doe',
        'title' : 'End of the World',
        'content':'Data about the post',
        'date_posted' : 'April 20, 2018'
    }
]

@app.route("/")
def hello():
    return render_template('home.html', title="My homepage", posts=posts)


@app.route("/about")
def about():
    return render_template('about.html',title='About Page')

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Vlad Snisar',
        'title': 'My first flask blog page',
        'content': 'This is my first flask blog page, here you can view posts made by other users, \
            create your own ones, register, authenticate, change profile photo and do other cool stuff. Feel free to explore.',
        'date_posted': 'june 01, 2022'
    },
    {
        'author': 'Guido van Rossum',
        'title': 'Python programming language',
        'content': 'I\'m a father of Python programming language. \
            Van Rossum thought he needed a name that was short, unique, \
                and slightly mysterious, so he decided to call the language Python.',
        'date_posted': 'June 01, 2022'
    }
]

@app.route("/home")
@app.route("/")
def hello():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")
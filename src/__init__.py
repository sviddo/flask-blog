from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, RegistrationForm
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "e5629898b9e96d1021f1433a665bb77b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def __str__(self):
        return f"User {self.username}, {self.email}, {self.image_file}"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __str__(self):
        return f"User {self.title}, {self.date_posted}"

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
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def log_in():
    form = LoginForm()
    if form.validate_on_submit():                                                                       #
        if form.email.data == "test@test.com" and form.password.data == "password":                     #
            flash('You have been logged in!', 'success')                                                #  simulating authentication
            return redirect(url_for('home'))                                                            #
        else:                                                                                           #
            flash('Authentication was rejected. Please, check your username and password', 'danger')    #                                                              
    return render_template('login.html', title='Log in', form=form)
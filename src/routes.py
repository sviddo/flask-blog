from flask import render_template, url_for, flash, redirect
from src import app, db, bcrypt
from src.forms import LoginForm, RegistrationForm
from src.models import User, Post


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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! Now you are able to log in', 'success')
        return redirect(url_for('log_in'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def log_in():
    form = LoginForm()
    if form.validate_on_submit():                                                                       #                     
        if form.email.data == "test@test.com" and form.password.data == "password":                     #
            flash('You have been logged in!', 'success')                                                #  authentication simulation
            return redirect(url_for('home'))                                                            #  
        else:                                                                                           #
            flash('Authentication was rejected. Please, check your username and password', 'danger')    #                                                           
    return render_template('login.html', title='Log in', form=form)
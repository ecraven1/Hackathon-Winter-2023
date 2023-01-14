from flask import render_template, url_for, flash, redirect
from fitvidapphackathon import app
from fitvidapphackathon.forms import RegistrationForm, LoginForm
from fitvidapphackathon.models import User, NewExercise



new_exercises = [
    {   'instructor': 'Matt',
        'exercise_name': 'Exercise Name 1',
        'content': 'First new exercise content',
        'date_posted': 'April 20, 2022'
    },
    {   'instructor': 'Emily',
        'exercise_name': 'Exercise Name 2',
        'content': 'Second new exercise content',
        'date_posted': 'May 3, 2022'
    },
    {   'instructor': 'Chris',
        'exercise_name': 'Exercise Name 2',
        'content': 'Second new exercise content',
        'date_posted': 'May 21, 2022'
    },
    {   'instructor': 'Monika',
        'exercise_name': 'Exercise Name 2',
        'content': 'Second new exercise content',
        'date_posted': 'June 1, 2022'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', new_exercises=new_exercises)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Pelase check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

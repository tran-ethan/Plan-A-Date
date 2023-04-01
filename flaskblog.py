from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import DataForm
from logic import data

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html', data=data)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = DataForm()
    if form.validate_on_submit():
        # Get the data submitted by the user
        gender = form.gender.data
        age = form.age.data
        day = form.day.data
        time = form.time.data
        interests = form.interests.data
        postal_code = form.postal_code.data
        min_budget = form.min_budget.data
        max_budget = form.max_budget.data
        return render_template('home.html', data=data)

    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import DataForm
from logic import get_places, get_lat_long

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/", methods=['GET', 'POST'])
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
        print(gender)
        print(age)
        print(day)
        print(time)
        print(interests)
        print(min_budget)
        coordinates = get_lat_long(postal_code)
        places = get_places(gender=gender, age=age, day=day, time=time, interests=interests, min_price=min_budget,
                            max_price=max_budget, location=coordinates)
        return render_template('home.html', data=places)

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

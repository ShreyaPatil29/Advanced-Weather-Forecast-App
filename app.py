import sqlite3
from unicodedata import name
from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from flask_sqlalchemy import SQLAlchemy

# configurations
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///weather.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "bruhidk"

db = SQLAlchemy(app)

# database model
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


# get 5-day forecast data
def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid=158064612e2835871e52b1a3e41e9923"
    r = requests.get(url).json()
    return r


# home page
@app.route("/")
def index_get():
    cities = City.query.all()
    weather_data = []

    for city in cities:
        r = get_weather_data(city.name)

        if "list" in r:
            forecast = []

            for i in range(0, 40, 8):   # every 24 hours = 8 records
                day = {
                    "date": r["list"][i]["dt_txt"],
                    "temperature": r["list"][i]["main"]["temp"],
                    "description": r["list"][i]["weather"][0]["description"],
                    "icon": r["list"][i]["weather"][0]["icon"]
                }
                forecast.append(day)

            weather = {
                "city": city.name,
                "forecast": forecast
            }

            weather_data.append(weather)

    return render_template("index.html", weather_data=weather_data)


# add city
@app.route("/", methods=["POST"])
def index_post():
    err_msg = ""
    new_city = request.form.get("city")

    if new_city:
        existing_city = City.query.filter_by(name=new_city).first()

        if not existing_city:
            new_city_data = get_weather_data(new_city)

            if new_city_data["cod"] == "200":
                nw_city_obj = City(name=new_city)
                db.session.add(nw_city_obj)
                db.session.commit()
            else:
                err_msg = "City doesn't exist in the world"
        else:
            err_msg = "City already exists in database"

    if err_msg:
        flash(err_msg, "error")
    else:
        flash("City Added Successfully", "success")

    return redirect(url_for("index_get"))


# delete city
@app.route("/delete/<name>")
def delete_city(name):
    city = City.query.filter_by(name=name).first()

    if city:
        db.session.delete(city)
        db.session.commit()
        flash(f"Successfully Deleted {city.name}", "success")

    return redirect(url_for("index_get"))


# run app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
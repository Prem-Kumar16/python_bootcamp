from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    current_yr = datetime.datetime.now().year
    my_name = "Prem Kumar S"
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, yr=current_yr, name=my_name)

@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    age_url = f"https://api.agify.io?name={name}"

    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    random_gender = gender_data["gender"]

    age_response = requests.get(age_url)
    age_data = age_response.json()
    random_age = age_data["age"]

    return render_template("guess.html", person_name=name, gender=random_gender, age=random_age)


if __name__ == "__main__":
    app.run(debug=True)

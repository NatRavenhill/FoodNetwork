from flask import Flask, request
from flask import render_template

from login import LoginForm
from registration import RegistrationForm

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/foodbank")
def foodbank():
    registrationForm = RegistrationForm(request.form);
    loginForm = LoginForm(request.form);
    return render_template('foodbank.html', registrationForm=registrationForm, loginForm=loginForm)

@app.route("/donator")
def donator():
    return render_template('donator.html')

@app.route("/receiver")
def receiver():
    return render_template('receiver.html')

if __name__ == "__main__":
    app.debug = True
    app.run()

from flask import Flask, request, flash, redirect
from flask import render_template

from login import LoginForm
from registration import RegistrationForm

app = Flask(__name__)
app.secret_key = 'gfdhajghjarejw ophyugipefqh984372824'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/foodbank')
def foodbank():
    registrationForm = RegistrationForm();
    loginForm = LoginForm();

    return render_template('foodbank.html', registrationForm=registrationForm, loginForm=loginForm)

@app.route('/register', methods=['POST'])
def register():
    registrationForm = RegistrationForm(request.form)
    if registrationForm.validate():
        flash('You\'ve been registered!', 'success')
    else:
        flash('Registration failed :(', 'error')
    return redirect('/foodbank')

@app.route('/donator')
def donator():
    return render_template('donator.html')

@app.route('/receiver')
def receiver():
    return render_template('receiver.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

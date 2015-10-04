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

    user = request.args.get("user")
    if user:
        return render_template('foodbank.html', user=user)
    else:
        return render_template('foodbankforms.html', registrationForm=registrationForm, loginForm=loginForm)

@app.route('/register', methods=['POST'])
def register():
    registrationForm = RegistrationForm(request.form)
    if registrationForm.validate():
        flash('You\'ve been registered!', 'success')
    else:
        flash('Registration failed :(', 'error')
    return redirect('/foodbank')

@app.route('/login', methods=['POST'])
def login():
    loginForm = LoginForm(request.form)
    if loginForm.validate():
        flash('You\'ve been logged in!', 'success')
        return redirect('/foodbank?user=' + loginForm.username.data)
    else:
        flash('Login failed :(', 'error')
        return redirect('/foodbank')

@app.route('/donator')
def donator():
    mostNeededItems = [
        {'name': 'Milk', 'colour': 'danger'},
        {'name': 'Pasta', 'colour': 'warning'},
        {'name': 'Baked beans', 'colour': 'success'}
    ]
    return render_template('donator.html', mostNeededItems=mostNeededItems)

@app.route('/receiver')
def receiver():
    return render_template('esri.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

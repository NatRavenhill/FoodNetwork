from flask import Flask, request, flash, redirect
from flask import render_template

from login import LoginForm
from registration import RegistrationForm
from text import TextForm

from twilio.rest import TwilioRestClient

import braintree
import config

app = Flask(__name__)

#info for twilio
client = TwilioRestClient(config.account_sid, config.auth_token)

#info for braintree
braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  config.merchant_id,
                                  config.public_key,
                                  config.private_key)
								 
#send client token to client
@app.route("/client_token", methods=["GET"])
def client_token():
  return braintree.ClientToken.generate()
  

@app.route("/checkout", methods=["POST"])
def create_purchase():
  nonce = request.form["payment_method_nonce"]
  result = braintree.Transaction.sale({
    "amount": "10.00",
    "payment_method_nonce": "fake-valid-nonce"
  })
  if result.is_success:
      return "<h1>Success! Thank You for your Donation!</h1>"
  else:
       return "<h1>Error: {0}</h1>".format(result.message)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/foodbank')
def foodbank():
    registrationForm = RegistrationForm();
    loginForm = LoginForm();
    textForm = TextForm();
    user = request.args.get("user")
    if user:
        return render_template('foodbankText.html', user=user, textForm = textForm)
    else:
        return render_template('foodbankforms.html', registrationForm=registrationForm, loginForm=loginForm )

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
	

@app.route('/foodbankText', methods=['GET', 'POST'])
def text():
    textForm = TextForm(request.form)
    if request.method == 'POST' and  textForm.validate() :
       message = client.messages.create(to="+447784456027", from_="+441922214241", body = textForm.foodbankName.data + " needs some more " + textForm.food.data)
       return render_template('foodbankText.html', textForm = textForm, success=True)
    else:
       return render_template('foodbankText.html', textForm = textForm, success=False)


if __name__ == '__main__':
    app.debug = True
    app.run()

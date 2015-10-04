from flask import Flask, request, flash, redirect
from flask import render_template

from login import LoginForm
from registration import RegistrationForm
from text import TextForm

from twilio.rest import TwilioRestClient

import braintree

app = Flask(__name__)
app.secret_key = 'gfdhajghjarejw ophyugipefqh984372824'

#info for twilio
account_sid = "ACabbdc6a9c7645d6a38069ac3fe6c99c5"
auth_token = "04670510815d4503cdf5f8d5414bdb8a"
client = TwilioRestClient(account_sid, auth_token)

#info for braintree
braintree.Configuration.configure(braintree.Environment.Sandbox,
                                   merchant_id="yb48tgk36vmy35zw",
	                     public_key = "ddqsprrw4377dv3f",
                                   private_key="8873838a196e6d67b45a5d2d6ae142d9")
								 
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

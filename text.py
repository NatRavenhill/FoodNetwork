from wtforms import Form, StringField, PasswordField, validators

class TextForm(Form):
	foodbankName = StringField('FoodBank Name', [validators.Required()])
	food = StringField('Food Needed' , [validators.Required()])
	
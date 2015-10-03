from wtforms import Form, StringField, PasswordField, validators

class RegistrationForm(Form):
    username = StringField('Email address', [validators.required(), validators.Length(min=4, max=25)])
    password = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat password')

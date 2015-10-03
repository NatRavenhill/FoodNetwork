from wtforms import Form, StringField, PasswordField, validators

class LoginForm(Form):
    username = StringField('Email address', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])

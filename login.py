from wtforms import Form, StringField, validators

class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])

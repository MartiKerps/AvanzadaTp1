from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Length

class RegisterForm(FlaskForm):
    username = StringField("Nombre Completo:", validators=[DataRequired()])
    email = StringField(label='Email: ', validators=[DataRequired(), Email()])
    password = PasswordField(label='Contraseña: ', validators=[DataRequired(), Length(min=8), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField(label='Repita su contraseña:', validators=[DataRequired()])
    submit = SubmitField(label='Registrarse')

class LoginForm(FlaskForm):
    email = StringField(label='Ingrese su Email: ', validators=[DataRequired(), Email()])
    password = PasswordField(label='Contraseña: ', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Ingresar')

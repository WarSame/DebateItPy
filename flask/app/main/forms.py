from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email


class EmailPasswordForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])


class CreateCommunityForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    description = StringField("Description")


class CreateDebateForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    text = StringField("Text")
    community_id = IntegerField("Community_id", validators=[DataRequired()])

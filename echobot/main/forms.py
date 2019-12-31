from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL, Required


class WebhookUrlForm(FlaskForm):
    webhook_url = StringField("Webhook Url", validators=[URL(), Required()])
    submit = SubmitField("Submit")

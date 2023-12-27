from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, URL, Length, Email
from flask_ckeditor import CKEditorField


class ContactForm(FlaskForm):
    name = StringField("", render_kw={"placeholder": "Your Name", "class": "col-md-6 form-group", "style": "text"},
                       validators=[DataRequired()])
    email = EmailField("", render_kw={"placeholder": "Your Email", "class": "col-md-6 form-group mt-3 mt-md-0",
                                      "style": "text"}, validators=[DataRequired()])
    subject = StringField("", render_kw={"placeholder": "Subject"}, )
    message = CKEditorField("", render_kw={"placeholder": "Your Message", "rows": "5"}, validators=[DataRequired()])
    submit = SubmitField("Send Message", render_kw={"style":
                                                        "background-color: #34b7a7; "
                                                        "border: 0; "
                                                        "padding: 10px 30px 12px 30px; "
                                                        "color:  #fff;"
                                                        "transition: 0.4s;"
                                                        "border-radius: 50px;"})

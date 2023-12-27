import os
import smtplib

from flask import Flask, render_template, url_for, flash, redirect
from flask_bootstrap import Bootstrap5
from forms import ContactForm
from flask_ckeditor import CKEditor

my_email = os.environ.get("my_email")
# print(my_email)
gmail_password = os.environ.get("PSW")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
# print(app.config["SECRET_KEY"])
ckeditor = CKEditor(app)
Bootstrap5(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/resume')
def resume():
    return render_template("resume.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        name = contact_form.name.data,
        email = contact_form.email.data,
        subject = contact_form.subject.data,
        message = contact_form.message.data,
        entire_message = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        print(entire_message)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=gmail_password)
            mail_to = os.environ.get("MAIL_TO")
            connection.sendmail(from_addr=my_email,
                                to_addrs=mail_to,
                                msg=f"Subject:{subject}\n\n{entire_message}")
        flash("Your message has been delivered!")
        return redirect(url_for('home'))
    return render_template("contact.html", form=contact_form)


@app.route('/skills')
def skills():
    return render_template("skills.html")


if __name__ == "__main__":
    app.run(debug=True)

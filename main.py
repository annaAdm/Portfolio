import os

from flask import Flask, render_template, url_for, flash, redirect
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
# print(app.config["SECRET_KEY"])
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


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/skills')
def skills():
    return render_template("skills.html")


if __name__ == "__main__":
    app.run(debug=True)

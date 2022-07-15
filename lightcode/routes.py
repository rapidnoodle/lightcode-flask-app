from lightcode import app
from flask import render_template
from markupsafe import escape  # this function renders html as text


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route('/services')
def services_page():
    return render_template("services.html")


@app.route("/work")
def work_page():
    return render_template("work.html")


@app.route('/contact')
def contact_page():
    return render_template("contact.html")

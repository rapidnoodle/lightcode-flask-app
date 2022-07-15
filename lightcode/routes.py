from lightcode import app, db
from flask import redirect, render_template, request, url_for
from lightcode.models import ContactResponse
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


@app.route('/contact', methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        message = ContactResponse(
            first_name=request.form.get("first_name"),
            last_name=request.form.get("last_name"),
            email=request.form.get("email"),
            subject=request.form.get("subject"),
            message=request.form.get("message")
        )
        db.session.add(message)
        db.session.commit()
        return redirect(url_for("thank_you_page"))
    return render_template("contact.html")


@app.route('/thank-you')
def thank_you_page():
    return render_template("thank_you.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

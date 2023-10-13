from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    data = request.form
    print(data)
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return "<p>Logout init</p>"


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email must be greater than 4 characters", category="error")
        elif len(firstName) < 2:
            flash("First name must be greater than 1 character", category="error")
        elif password1 != password2:
            flash("Your passwords must match to each other", category="error")
        elif len(password1) < 7:
            flash(
                "Password is too short, it should be at leat 7 characters ", category="error")
        else:
            # add user to db
            new_user = User(email=email, first_name=firstName,
                            password=generate_password_hash(password1, method='sha256'))

            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully", category="success")
            return redirect(url_for("views.home"))

    return render_template("signup.html")


# for testing purposes
# passing any vars

# @auth.route("/login")
# def login():
#     return render_template("login.html", text="testing", user="tim")

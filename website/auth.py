from flask import Blueprint

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return "<p>Login init</p>"


@auth.route("/logout")
def logout():
    return "<p>Logout init</p>"


@auth.route("/signup")
def signup():
    return "<p>Signup init</p>"

from flask import Blueprint
from flask import render_template, request

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html")

@main.route("/userlogin")
def userlogin():
    return render_template("userlogin.html")

@main.route("/businesslogin")
def businesslogin():
    return render_template("businesslogin.html")

@main.route("/contact")
def contact():
    return render_template("contact.html")

@main.route("/about")
def about():
    return render_template("about.html")
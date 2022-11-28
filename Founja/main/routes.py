from flask import Blueprint
from flask import render_template, flash, redirect,  url_for, request, abort
from Founja.main.forms import (RegistrationForm, LoginForm)
#from Founja.models import User, Post


main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html")

@main.route("/userlogin",methods=["GET", "POST"])
def userlogin():
    form = LoginForm()
    return render_template("userlogin.html", title="User_login", form=form)

@main.route("/businesslogin")
def businesslogin():
    return render_template("businesslogin.html")

@main.route("/contact")
def contact():
    return render_template("contact.html")

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)
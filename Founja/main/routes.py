from flask import Blueprint
from flask import render_template, flash, redirect,  url_for, request, abort
from Founja.main.forms import (ClientRegistrationForm, BusinessRegistrationForm, ClientLoginForm, BusinessLoginForm)
#from Founja.models import User, Post


main = Blueprint("main", __name__)

#ROOT/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html")
@main.route("/contact")
def contact():
    return render_template("contact.html")

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/client_register", methods=["GET", "POST"])
def client_register():
    form = ClientRegistrationForm()
    return render_template("register.html", title="Register", form=form)

#CLIENT///////////////////////////////////////////////////////////////////////////////////////////////////////////////
@main.route("/client_register", methods=["GET", "POST"])
def client_register():
    form = ClientRegistrationForm()
    return render_template("client_template/client_register.html", title="client_register", form=form)

@main.route("/client_login",methods=["GET", "POST"])
def client_login():
    form = ClientLoginForm()
    return render_template("client_template/client_login.html", title="client_login", form=form)

#BUSINESS////////////////////////////////////////////////////////////////////////////////////////////////////////////
@main.route("/business_register", methods=["GET", "POST"])
def business_register():
    form = BusinessRegistrationForm()
    return render_template("business_template/business_register.html", title="business_register", form=form)

@main.route("/business_login",methods=["GET", "POST"])
def business_login():
    form = BusinessLoginForm()
    return render_template("business_template/business_login.html", title="business_login", form=form)
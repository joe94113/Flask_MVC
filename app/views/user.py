from flask import render_template
from flask import request
from app.models.user import User, _create


class Views:
    def index():
        return render_template("users/index.html")

    def new():
        return render_template("users/new.html")

    def create():
        username = request.form["username"]
        email = request.form["email"]
        _create(username, email)
        # call models
        return "User creation successful"

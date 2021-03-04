from flask import render_template
from flask import request
from app.models.user import User, _create, _update, _destroy


class Views:
    def index():
        return render_template("users/index.html")

    def new():
        user = User()
        return render_template("users/new.html", user=user)

    def create():
        username = request.form["username"]
        email = request.form["email"]
        _create(username, email)
        # call models
        return "User creation successful"

    def show(id):
        user = User.query.filter_by(id=id).first()
        return render_template("users/show.html", user=user)

    def edit(id):
        user = User.query.filter_by(id=id).first()
        return render_template("users/edit.html", user=user)

    def update(id):
        email = request.form["email"]
        _update(id, email)
        return

    def destroy(id):
        _destroy(id)
        return

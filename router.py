from flask import url_for

from app import app
from app.views.user import Views


@app.route("/", methods=["GET"])
def index():
    return Views.index()


@app.route("/new", methods=["GET"])
def new():
    return Views.new()


@app.route("/create", methods=["POST"])  # 新增資料
def create():
    return Views.create()


@app.route('/<int:id>', methods=["GET"])  # 顯示資料
def show(id):
    return Views.show(id)


@app.route("/<int:id>/edit", methods=["GET"])  # 修改資料
def edit(id):
    url_delete = url_for("destroy", id=id)  # 得到刪除功能裝飾器function的路由
    url_update = url_for("update", id=id)   # 得到更新功能裝飾器function的路由
    return Views.edit(id, url_delete=url_delete, url_update=url_update)


@app.route("/<int:id>", methods=["POST"])  # 更新資廖
def update(id):
    Views.update(id)
    return "User update successful"


@app.route("/<int:id>/delete", methods=["POST"])  # 刪除資料
def destroy(id):
    Views.destroy(id)
    return "User deleted"

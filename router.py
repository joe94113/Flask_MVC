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


@app.route("/<int:id>/edit", methods=["GET"])  # 修改資料
def edit(id):
    return Views.edit(id)


@app.route("/<int:id>", methods=["POST"])  # 更新資廖
def update(id):
    Views.update(id)
    return "User update successful"



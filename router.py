from app import app
from app.views.user import Views


@app.route("/", methods=["GET"])
def index():
    return Views.index()

@app.route("/new", methods=["GET"])
def new():
    return Views.new()

@app.route("/create", methods=["POST"])
def create():
    return Views.create()
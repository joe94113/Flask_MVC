from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)  # 初始化flask
app.config.from_object("config")

db = SQLAlchemy(app)  # 初始化

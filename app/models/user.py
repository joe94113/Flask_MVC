from sqlalchemy import desc

from .. import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement="auto", default=1)  # 遇到問題id不會自動遞增
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    # 儲存進資料庫


def _create(username, email):
    if User.query.order_by(desc('id')).first():
        oldUser = User.query.order_by(desc('id')).first()
        user = User(id=oldUser.id + 1, username=username, email=email)
    else:
        user = User(id=1, username=username, email=email)

    db.session.add(user)
    db.session.commit()
    return


# 更新資料庫
def _update(id, email):
    user = User.query.filter_by(id=id).first()  # 讀取資料
    user.email = email  # 更新email
    db.session.commit()  # 變更資料庫資料
    return


def _destroy(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)  # 刪除資料
    db.session.commit()
    return


def __init__(self, username=None, email=None):
    self.username = username
    self.email = email


def __repr__(self):
    return '<User %r>' % self.username

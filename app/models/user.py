from .. import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)


# 儲存進資料庫
def _create(username, email):
    user = User(id=1, username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return


# 更新資料庫
def _update(id, email):
    user = User.query.filter_by(id=id).first()  # 從user表格找到id
    user.email = email  # 更新email
    db.session.commit()  # 變更資料庫資料
    return

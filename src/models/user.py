from src import db

# 定义用户表Model


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), default='', nullable=False)
    email = db.Column(db.String(64), default='', nullable=False)
    status = db.Column(db.Integer, default=0, nullable=False)

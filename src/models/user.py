from src import db

# 定义日期的默认值
DEF_DATE = '1970-02-01 00:00:00'

# 定义用户表Model


class User(db.Model):
    __tablename__ = 'dm_developer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), default='', nullable=False)
    email = db.Column(db.String(64), default='', nullable=False)
    business_group = db.Column(db.String(64), default='', nullable=False)
    status = db.Column(db.Integer, default=0, nullable=False)
    created_at = db.Column(db.Integer, default=DEF_DATE, nullable=False)

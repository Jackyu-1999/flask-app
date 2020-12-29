from app6 import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    passwd = db.Column(db.String(64))


    def __repr__(self):
        return "<Role %r>"% self.name

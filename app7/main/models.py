from app7 import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    passwd = db.Column(db.String(64))


    def __repr__(self):
        return "<Role %r>"% self.name

        
class Comments(db.Model):
	__tablename__ = "Comments"
	id = db.Column(db.Integer, primary_key=True)
	says = db.Column(db.Text)
	datetime = db.Column(db.DATETIME)
	user_id = db.Column(db.Integer)

	def __repr__(self):
		return "<comment %d>"% self.id
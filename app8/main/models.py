from app8 import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    passwd = db.Column(db.String(64))
    comments = db.relation("Comments", backeref='user')


    def __repr__(self):
        return "<Role %r>"% self.name

        
class Comments(db.Model):
	__tablename__ = "Comments"
	id = db.Column(db.Integer, primary_key=True)
	says = db.Column(db.Text)
	datetime = db.Column(db.DATETIME)
	user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

	def __repr__(self):
		return "<comment %d>"% self.id
	
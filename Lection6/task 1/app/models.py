from app import db

class users(db.Model):
    name = db.Column(db.String(64), primary_key = True)
    password = db.Column(db.String(256))



from app import db

class users(db.Model):
    name = db.Column(db.String(64), primary_key = True)
    password = db.Column(db.String(256))

class messages(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(256))
    message = db.Column(db.String(256))
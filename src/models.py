from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class URLS(db.Model):
    __tablename__ = "urls"

    id = db.Column(db.Integer, primary_key=True)
    short = db.Column(db.String, unique=True, nullable=True)
    original = db.Column(db.String, unique=True, nullable=False)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class URLS(db.Model):
    __tablename__ = "urls"
    id = db.Column(db.Integer, primary_key=True)
    short = db.Column(db.String, unique=True, nullable=True)
    original = db.Column(db.String, unique=True, nullable=False)

class AccessLog(db.Model):
    __tablename__ = "access_logs"
    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer, db.ForeignKey("urls.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

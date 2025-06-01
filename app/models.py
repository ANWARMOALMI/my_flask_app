from . import db

class License(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    license_key = db.Column(db.String(255), unique=True, nullable=False)
    device_name = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

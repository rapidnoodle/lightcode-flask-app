from lightcode import db
from datetime import datetime


class ContactResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(320), nullable=False)
    subject = db.Column(db.String(50), default="no subject")
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.email} - {self.subject}\n{self.message}"

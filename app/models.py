from . import db
from datetime import datetime

class UserLog(db.Model):
    _tablename_ = 'user_logs'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    ip_address = db.Column(db.String(45))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def _repr_(self):
        return f"<UserLog {self.id} - {self.username}>"
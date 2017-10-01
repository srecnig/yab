from . import db

from datetime import datetime

from sqlalchemy.dialects.postgresql import JSONB

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    meta = db.Column(JSONB, default=lambda: {})
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Post %r>' % self.title

from .db import environment, SCHEMA, add_prefix_for_prod
from datetime import datetime
from app.models import db

class Portfolio(db.Model):
    __tablename__ = 'portfolios'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    balance = db.Column(db.Float, default=10000.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', back_populates='portfolios')
    stock_holdings = db.relationship('StockHolding', back_populates='portfolio', cascade='all, delete-orphan')
    transactions = db.relationship('Transaction', back_populates='portfolio', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "balance": self.balance,
            "created_at": self.created_at.isoformat()
        }
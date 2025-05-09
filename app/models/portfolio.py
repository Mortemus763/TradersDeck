from app.models import db
from datetime import datetime

class Portfolio(db.Model):
    __tablename__ = 'portfolios'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    balance = db.Column(db.Float, default=10000.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', back_populates='portfolios')
    stock_holdings = db.relationship('StockHolding', back_populates='portfolio', cascade='all, delete-orphan')
    transactions = db.relationship('Transaction', back_populates='portfolio', cascade='all, delete-orphan')

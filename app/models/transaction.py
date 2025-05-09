from app.models import db
from datetime import datetime

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(10), nullable=False)
    shares = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(4), nullable=False)  # 'BUY' or 'SELL'
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'), nullable=False)
    portfolio = db.relationship('Portfolio', back_populates='transactions')

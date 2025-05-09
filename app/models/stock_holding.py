from app.models import db

class StockHolding(db.Model):
    __tablename__ = 'stock_holdings'

    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(10), nullable=False)
    shares = db.Column(db.Integer, nullable=False)
    avg_price = db.Column(db.Float, nullable=False)

    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'), nullable=False)
    portfolio = db.relationship('Portfolio', back_populates='stock_holdings')

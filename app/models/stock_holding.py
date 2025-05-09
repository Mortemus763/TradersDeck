from .db import db, environment, SCHEMA, add_prefix_for_prod

class StockHolding(db.Model):
    __tablename__ = 'stock_holdings'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(10), nullable=False)
    shares = db.Column(db.Integer, nullable=False)
    avg_price = db.Column(db.Float, nullable=False)

    portfolio_id = db.Column(
        db.Integer,
        db.ForeignKey(add_prefix_for_prod('portfolios.id')),
        nullable=False
    )
    portfolio = db.relationship('Portfolio', back_populates='stock_holdings')

    def to_dict(self):
        return {
            "id": self.id,
            "ticker": self.ticker,
            "shares": self.shares,
            "avg_price": self.avg_price,
            "portfolio_id": self.portfolio_id
        }
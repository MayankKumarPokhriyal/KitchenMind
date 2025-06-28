from app import db
from datetime import datetime

class PreppedMeal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(100), nullable=False)
    portions = db.Column(db.Integer, nullable=False)
    expiry_date = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f"<PreppedMeal {self.recipe_name}>"
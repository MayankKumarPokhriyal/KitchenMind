from app import db

class UserSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    protein = db.Column(db.Float, nullable=True)
    carbs = db.Column(db.Float, nullable=True)
    fats = db.Column(db.Float, nullable=True)
    calories = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"<UserSettings>"
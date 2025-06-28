import os

class Config:
    SECRET_KEY = 'your-secret-key'  # Change this in production
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/kitchenmind.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
    RECIPES_FILE = os.path.join(DATA_DIR, 'recipes.json')
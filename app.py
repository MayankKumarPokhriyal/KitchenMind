from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import routes after app initialization to avoid circular imports
from routes import inventory_routes, suggest_routes, log_routes, meal_prep_routes, settings_routes

# Register blueprints
app.register_blueprint(inventory_routes.bp)
app.register_blueprint(suggest_routes.bp)
app.register_blueprint(log_routes.bp)
app.register_blueprint(meal_prep_routes.bp)
app.register_blueprint(settings_routes.bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
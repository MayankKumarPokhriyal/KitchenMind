# KitchenMind

A simple Flask-based web application to manage kitchen inventory, suggest meals based on available ingredients, track nutrition, and plan meal prep.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd kitchenmind
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create data directory and database**:
   ```bash
   mkdir db
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. Open your browser and navigate to `http://127.0.0.1:5000`.

## Features

- **Inventory Management**: Add, edit, delete grocery items with name, quantity, unit, and optional expiry date.
- **Meal Suggestions**: Suggests recipes based on available inventory.
- **Nutrition Tracking**: Logs meals and tracks daily protein, carbs, fats, and calories.
- **Meal Prep**: Plan meals in advance and update inventory accordingly.
- **Daily Goals**: Set and track daily macro and calorie goals.

## Folder Structure

- `app.py`: Main Flask application.
- `config.py`: Configuration settings.
- `static/`: CSS and JS files.
- `templates/`: HTML templates using Jinja2.
- `data/`: JSON file for recipes.
- `models/`: SQLAlchemy models for database.
- `routes/`: Flask blueprints for routing.
- `utils/`: Utility functions (e.g., macro calculations).
- `db/`: SQLite database.

## Requirements

- Python 3.8+
- Flask
- Flask-SQLAlchemy

## Notes

- Ensure the `data` directory contains `recipes.json` with valid recipe data.
- The app uses TailwindCSS via CDN for styling.
- SQLite database is created automatically on first run.
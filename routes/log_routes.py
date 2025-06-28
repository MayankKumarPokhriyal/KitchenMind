from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from models.meals import MealLog
import json
from datetime import datetime

bp = Blueprint('log_routes', __name__)

@bp.route('/log_meal', methods=['GET', 'POST'])
def log_meal():
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        portions = int(request.form['portions'])
        
        # Load recipes to get macros
        with open(app.config['RECIPES_FILE'], 'r') as f:
            recipes = json.load(f)
        
        recipe = next((r for r in recipes if r['name'] == recipe_name), None)
        if recipe:
            macros = recipe['macros']
            meal_log = MealLog(
                recipe_name=recipe_name,
                portions=portions,
                protein=macros['protein'] * portions,
                carbs=macros['carbs'] * portions,
                fats=macros['fats'] * portions,
                calories=macros['calories'] * portions
            )
            db.session.add(meal_log)
            db.session.commit()
            return redirect(url_for('log_routes.log_meal'))
    
    meal_logs = MealLog.query.all()
    return render_template('log_meal.html', meal_logs=meal_logs)
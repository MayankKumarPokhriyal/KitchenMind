from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from models.prep import PreppedMeal
from models.inventory import InventoryItem
import json
from datetime import datetime

bp = Blueprint('meal_prep_routes', __name__)

@bp.route('/meal_prep', methods=['GET', 'POST'])
def meal_prep():
    with open(app.config['RECIPES_FILE'], 'r') as f:
        recipes = json.load(f)
    
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        portions = int(request.form['portions'])
        expiry_date = request.form.get('expiry_date')
        expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d').date() if expiry_date else None
        
        # Update inventory
        recipe = next((r for r in recipes if r['name'] == recipe_name), None)
        if recipe:
            for ingredient in recipe['ingredients']:
                item = InventoryItem.query.filter_by(name=ingredient['name']).first()
                if item:
                    item.quantity -= ingredient['quantity'] * portions
                    if item.quantity <= 0:
                        db.session.delete(item)
                    else:
                        db.session.add(item)
            
            # Log prepped meal
            prepped_meal = PreppedMeal(recipe_name=recipe_name, portions=portions, expiry_date=expiry_date)
            db.session.add(prepped_meal)
            db.session.commit()
            return redirect(url_for('meal_prep_routes.meal_prep'))
    
    prepped_meals = PreppedMeal.query.all()
    return render_template('meal_prep.html', recipes=recipes, prepped_meals=prepped_meals)
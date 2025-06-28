from flask import Blueprint, render_template
import json
import os
from app import app
from models.inventory import InventoryItem

bp = Blueprint('suggest_routes', __name__)

@bp.route('/suggest_meals')
def suggest_meals():
    # Load recipes
    with open(app.config['RECIPES_FILE'], 'r') as f:
        recipes = json.load(f)
    
    # Get inventory
    inventory = {item.name: item.quantity for item in InventoryItem.query.all()}
    
    # Suggest meals
    suggestions = []
    for recipe in recipes:
        can_make = True
        for ingredient in recipe['ingredients']:
            if ingredient['name'] not in inventory or inventory[ingredient['name']] < ingredient['quantity']:
                can_make = False
                break
        if can_make:
            suggestions.append(recipe)
    
    return render_template('suggest_meals.html', suggestions=suggestions)
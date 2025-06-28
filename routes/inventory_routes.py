from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from models.inventory import InventoryItem
from datetime import datetime

bp = Blueprint('inventory_routes', __name__)

@bp.route('/')
def index():
    from models.meals import MealLog
    from models.settings import UserSettings
    from datetime import datetime, date
    settings = UserSettings.query.first() or UserSettings(protein=0, carbs=0, fats=0, calories=0)
    today = date.today()
    meal_logs = MealLog.query.filter(db.func.date(MealLog.date_logged) == today).all()
    consumed = {
        'protein': sum(log.protein * log.portions for log in meal_logs),
        'carbs': sum(log.carbs * log.portions for log in meal_logs),
        'fats': sum(log.fats * log.portions for log in meal_logs),
        'calories': sum(log.calories * log.portions for log in meal_logs)
    }
    goals = [
        ('protein', settings.protein or 0, consumed['protein']),
        ('carbs', settings.carbs or 0, consumed['carbs']),
        ('fats', settings.fats or 0, consumed['fats']),
        ('calories', settings.calories or 0, consumed['calories'])
    ]
    return render_template('index.html', goals=goals, consumed_calories=consumed['calories'])

@bp.route('/inventory', methods=['GET', 'POST'])
def inventory():
    if request.method == 'POST':
        name = request.form['name']
        quantity = float(request.form['quantity'])
        unit = request.form['unit']
        expiry_date = request.form.get('expiry_date')
        expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d').date() if expiry_date else None
        item = InventoryItem(name=name.lower(), quantity=quantity, unit=unit, expiry_date=expiry_date)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('inventory_routes.inventory'))
    items = InventoryItem.query.all()
    return render_template('inventory.html', items=items)

@bp.route('/inventory/edit/<int:item_id>', methods=['POST'])
def edit_item(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    item.quantity = float(request.form['quantity'])
    db.session.commit()
    return redirect(url_for('inventory_routes.inventory'))

@bp.route('/inventory/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('inventory_routes.inventory'))
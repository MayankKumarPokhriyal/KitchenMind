from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from models.settings import UserSettings

bp = Blueprint('settings_routes', __name__)

@bp.route('/settings', methods=['GET', 'POST'])
def settings():
    settings = UserSettings.query.first() or UserSettings()
    
    if request.method == 'POST':
        settings.protein = float(request.form['protein']) if request.form['protein'] else 0
        settings.carbs = float(request.form['carbs']) if request.form['carbs'] else 0
        settings.fats = float(request.form['fats']) if request.form['fats'] else 0
        settings.calories = float(request.form['calories']) if request.form['calories'] else 0
        if not settings.id:
            db.session.add(settings)
        db.session.commit()
        return redirect(url_for('settings_routes.settings'))
    
    return render_template('settings.html', goals=settings)
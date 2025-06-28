# Placeholder for macro calculation logic
# Currently, macros are stored directly in recipes.json
def calculate_macros(recipe, portions=1):
    macros = recipe['macros']
    return {
        'protein': macros['protein'] * portions,
        'carbs': macros['carbs'] * portions,
        'fats': macros['fats'] * portions,
        'calories': macros['calories'] * portions
    }
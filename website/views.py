from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@views.route('/add_meal')
def add_food():
    return render_template("add_food.html")
    
@views.route('/reports')
def reports():
    return render_template("reports.html")

@views.route('/custom_meals')
def custom_meals():
    return render_template("custom_meals.html")
# system_routes.py

from flask import Blueprint, render_template

system_bp = Blueprint('system', __name__)

@system_bp.route('/home')
def home():
    return render_template('pages/home.html')

@system_bp.route('/battery')
def battery():
    return render_template('pages/battery.html')

@system_bp.route('/gpu')
def gpu():
    return render_template('pages/gpu.html')

@system_bp.route('/temperature')
def temperature():  
    return render_template('pages/temperature.html')

@system_bp.route('/trends')
def trends():
    return render_template('pages/trends.html')

@system_bp.route('/scientific')
def scientific():
    return render_template('pages/scientific.html')

from flask import Blueprint, render_template, redirect, url_for, flash, request
from auth.auth_forms import RegisterForm, LoginForm
from auth.auth_models import User
from extensions import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash('Username already exists', 'danger')
            return redirect(url_for('auth.register'))
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registered successfully! Please log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('login.html', form=form, page='register')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            flash('Logged in successfully!', 'success')
            return redirect(url_for('system.home'))  # Later change this to your /home page
        flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form, page='login')

@auth_bp.route('/')
def index():
    return redirect(url_for('auth.login'))

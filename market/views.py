from flask import Flask,Blueprint,render_template,flash,url_for,redirect
from flask_login import login_required,current_user
from functools import wraps
from .models import Seller, User,Rider







views = Blueprint('views', __name__)
role = [
     User(user_role = 'user'),
    Seller(seller_role = 'seller'),
    Rider(rider_role = 'rider')
]

def login_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                flash('You need to be logged in to access this page.', 'error')
                return redirect(url_for('auth.rider_login'))
            if current_user.user_role != role:
                flash(f'Access denied. You need to be a {role} to access this page.', 'error')
                return redirect(url_for('auth.rider_login')) 
            return func(*args, **kwargs)
        return wrapper
    return decorator





@views.route('/',methods=['GET'])
def landing():
   
    
        return  render_template('landing_page.html')
    
@views.route('/home',methods=['GET'])
@login_required('user')
def home():
   
    
    return  render_template('home.html')


@views.route('/seller-home', methods=['GET'])
@login_required('seller')
def seller_home():
    
    
    return render_template('seller_page.html')

@views.route('/seller-dashboard', methods =['GET'])
@login_required('seller')
def seller_dashboard():
    
    return render_template('seller-dashboard.html')



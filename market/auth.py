from flask import Flask,Blueprint,render_template,request,flash,redirect,url_for,abort
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_required,logout_user,current_user,login_user
from .models import User,Seller,Rider
from . import db 

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        password = request.form.get('password')

        user = User.query.filter_by(user_email=email).first()
        if user:
            if check_password_hash(user.user_password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template('login.html')

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        state = request.form.get('states')

        user = User.query.filter_by(user_email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(user_email=email,  user_state = state , user_password=generate_password_hash(
                password1, method='scrypt'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User Account created!', category='success')
            return redirect(url_for('auth.login'))

    
    return render_template('sign-up.html')

@auth.route('/seller-login',methods=['GET','POST'])
def seller_login():
  
        if request.method == 'POST':
            email = request.form.get('email').lower()
            password = request.form.get('password')

            seller = Seller.query.filter_by(seller_email=email).first()
            if seller:
                if check_password_hash(seller.seller_password, password):
                    flash('Logged in successfully!', category='success')
                    login_user(seller, remember=True)
                    return redirect(url_for('views.seller_home'))
                else:
                    flash('Incorrect password, try again.', category='error')
            else:
                flash('Email does not exist.', category='error')
           
        return render_template('seller-login.html')
   

@auth.route('/rider-login',methods=['GET','POST'])
def rider_login():
  
        if request.method == 'POST':
            email = request.form.get('email').lower()
            password = request.form.get('password')

            user = Rider.query.filter_by(rider_email=email).first()
            if user:
                if check_password_hash(user.rider_password, password):
                    flash('Logged in successfully!', category='success')
                    login_user(user, remember=True)
                    return 
                else:
                    flash('Incorrect password, try again.', category='error')
            else:
                flash('Email does not exist.', category='error')
    
        return render_template('rider-login.html')
  
       

@auth.route('/seller-signUp',methods=['GET','POST'])
def seller_sign_up():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        name = request.form.get('name')
        last_name= request.form.get('last_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        state = request.form.get('states')

        seller = Seller.query.filter_by(seller_email=email).first()
        if seller:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_seller = Seller(seller_email=email, seller_state = state , seller_name = name , seller_last_name = last_name, user_role = 'seller' ,seller_password=generate_password_hash(
                password1,  method='scrypt'))
            db.session.add(new_seller)
            db.session.commit()
            login_user(new_seller, remember=True)
            flash('Seller Account created!', category='success')
            return redirect(url_for('auth.seller_login'))

    
    return render_template('seller-sign-up.html')

@auth.route('/rider-signUp',methods=['GET','POST'])
def rider_sign_up():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        name = request.form.get('name').capitalize()
        last_name= request.form.get('last_name').capitalize()
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        state = request.form.get('states')

        user = Rider.query.filter_by(rider_email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = Rider(rider_email=email, rider_name = name , rider_state = state ,user_role = 'rider', rider_last_name = last_name, rider_password=generate_password_hash(
                password1, method='scrypt'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Rider Account created!', category='success')
            return redirect(url_for('auth.rider_login'))

    
    return render_template('rider-sign-up.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', category= 'success')
    return redirect(url_for('auth.login'))
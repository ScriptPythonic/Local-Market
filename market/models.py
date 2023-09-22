from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(150), unique=True)
    user_password = db.Column(db.String(150))
    user_state = db.Column(db.String(120))
    user_role = 'user'
    
    
class Seller(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    seller_name =  db.Column(db.String(50))
    seller_last_name =  db.Column(db.String(150), unique=True)
    seller_email =  db.Column(db.String(150), unique=True)
    seller_password = db.Column(db.String(150))
    seller_state = db.Column(db.String(120))
    seller_role = 'seller' 
    
class Rider(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    rider_name =  db.Column(db.String(50))
    rider_last_name =  db.Column(db.String(150), unique=True)
    rider_email =  db.Column(db.String(150), unique=True)
    rider_password = db.Column(db.String(150))
    rider_state = db.Column(db.String(120))
    rider_role = 'rider'
   
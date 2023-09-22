from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "market.db"
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from .views import views
    from .auth import auth
    
    app.register_blueprint(auth,url_prefix='/auth')
    app.register_blueprint(views, url_prefix='/')
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User,Seller,Rider
    @login_manager.user_loader
    def load_user(user_id):
        user = User.query.get(int(user_id))
        if user:
            return user
      
        return  None
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

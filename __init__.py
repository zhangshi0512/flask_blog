from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


# import routes at the end to avoid circular imports
def register_routes_models():
    import routes
    import models


register_routes_models()


@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

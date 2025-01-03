from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
# from products import Products



app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "03bfaf552b371a917873f108"


class Base(DeclarativeBase):
  pass
    
db = SQLAlchemy(model_class=Base)
db.init_app(app)



from website import models
from website import routes
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(150), nullable=False, unique=True)
    last_name = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)

    def __init__(self, username, first_name, last_name,  email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)

#class Pokemon(db.Model):
    # name = db.Column(db.String(50), primary_key=True)
    # hp_stat = db.Column(db.Integer)
    # def_stat = db.Column(db.Integer)
    # atk_stat = db.Column(db.Integer)
    # poke_img = db.Column(db.String(300))
    # ability = db.Column(db.String(50))

    # def __init__(self, name, hp_stat, def_stat, atk_stat, poke_img, ability):
    #     self.name = name
    #     self.hp_stat = hp_stat
    #     self.def_stat = def_stat
    #     self.atk_stat = atk_stat
    #     self.poke_img = poke_img
    #     self.ability = ability
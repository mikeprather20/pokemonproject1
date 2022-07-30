#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

# class Post(db.Model):
#     pokemon = db.Column(db.String(50), nullable=False, unique=True)
#     post = db.relationship("Post", backref='author', lazy=True)

#     def __init__(self, pokemon):
#         self.pokemon = pokemon



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
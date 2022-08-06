from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager

from .poke.routes import poke
from .auth.routes import auth
from .prof.routes import prof


from .models import User
from .models import my5
from .models import Pokemon


app = Flask(__name__)
login = LoginManager()

@login.user_loader
def load_user(id):
    return User.query.get(id)

app.register_blueprint(poke)
app.register_blueprint(auth)
app.register_blueprint(prof)

app.config.from_object(Config)

from .models import db

db.init_app(app)
migrate = Migrate(app,db)
login.init_app(app)

login.login_view = 'auth.logIn'

from . import routes
from . import models
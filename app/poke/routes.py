from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import LoginForm, UserRegistrationForm, PokemonFinderForm
import requests

from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

from app.models import User

poke = Blueprint('poke', __name__, template_folder='poke_template')

from app.models import db

####################################

@poke.route('/pokemon', methods = ['GET', 'POST'])
def pokedex():
    form = PokemonFinderForm()
    my_dict = {}

    if request.method == "POST":
        poke_name = form.name.data

        url = f"https://pokeapi.co/api/v2/pokemon/{poke_name}"
        res = requests.get(url)
        if res.ok:
            data = res.json()
            my_dict = {
                'name': data['name'],
                'ability': data['abilities'][0]['ability']['name'],
                'img_url': data['sprites']['front_shiny'],
                'hp': data['stats'][0]['base_stat'],
                'attack': data['stats'][1]['base_stat'],
                'defense': data['stats'][2]['base_stat']
            }

    return render_template('pokemon.html', form = form, pokemon = my_dict)


################################


@poke.route('/login',methods = ["GET","POST"] )
def logIn():
    form = LoginForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    flash('Your logged in!', 'success')
                    login_user(user)
                else:
                    flash('Incorrect username or password.', 'danger')
            else:
                flash('Username does not exist.', 'danger')

    return render_template('login.html', form=form)


@poke.route('/logout')
def logOut():
    flash("You logged out.", 'success')
    logout_user()
    return redirect(url_for('poke.logIn'))






################################


@poke.route('/register')
def register():
    form = LoginForm()
    if request.method == "POST":
        print('POST request made')
        if form.validate():
            username = form.username.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = form.password.data

            user = User(username, first_name, last_name, email, password)

            db.session.add(user)
            db.session.commit()
            flash("Successfully registered.", 'success')
            return redirect(url_for('poke.logIn'))
        else:
            flash('Please fill in all requirements!', 'danger')
    return render_template('register.html', form = form)

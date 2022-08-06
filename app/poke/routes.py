from app.models import db, Pokemon
from flask import Blueprint, redirect, render_template, request, url_for, flash
from .forms import PokemonFinderForm
import requests
from flask_login import login_required, current_user

poke = Blueprint('poke', __name__, template_folder='poke_template')


##################################################################


@poke.route('/pokemon', methods=['GET', 'POST'])
def pokedex():
    form = PokemonFinderForm()
    poke_dict = {}
    caught = False
    if request.method == "POST":
        if form.validate():
            name = form.poke_name.data

            url = f"https://pokeapi.co/api/v2/pokemon/{name}"
            res = requests.get(url)
            data = res.json()
            poke_dict = {
                'img_url': data['sprites']['front_shiny'],
                'name': data['name'],
                'ability': data['abilities'][0]['ability']['name'],
                'hp': data['stats'][0]['base_stat'],
                'attack': data['stats'][1]['base_stat'],
                'defense': data['stats'][2]['base_stat']
            }

            pokemon = Pokemon.query.filter_by(name=poke_dict['name']).first()
            if not pokemon:
                pokemon = Pokemon(poke_dict['img_url'], poke_dict['name'], poke_dict['ability'], poke_dict['hp'], poke_dict['attack'], poke_dict['defense'])
                db.session.add(pokemon)
                db.session.commit()

            if current_user.team.filter_by(name=pokemon.name).first():
                caught = True

    return render_template('pokemon.html', form=form, poke_dict=poke_dict, caught=caught)


##############################################################

@poke.route('/catch/<string:poke_name>', methods=['GET'])
def catchpoke(poke_name):
    pokemon = Pokemon.query.filter_by(name=poke_name).first()
    if len(current_user.team.all()) < 5:
        current_user.team.append(pokemon)
        db.session.commit()
    else:
        flash('Your team is FULL!', 'danger')
        return redirect(url_for('poke.user_team'))
    return redirect(url_for('poke.pokedex'))


##############################################################

@poke.route('/release/<string:poke_name>', methods=['GET'])
def releasepoke(poke_name):
    pokemon = Pokemon.query.filter_by(name=poke_name).first()
    current_user.team.remove(pokemon)
    db.session.commit()
    return redirect(url_for('poke.user_team'))

##############################################################

@poke.route('/myteam', methods=['GET'])
def user_team():
    team = current_user.team.all()
    return render_template('myteam.html', team=team)

##############################################################

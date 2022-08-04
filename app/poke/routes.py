from app.models import My5, db, Pokemon
from flask import Blueprint, render_template, request
from .forms import PokemonFinderForm
import requests
from flask_login import login_required, current_user

poke = Blueprint('poke', __name__, template_folder='poke_template')


##################################################################


@poke.route('/pokemon', methods=['GET', 'POST'])
def pokedex():
    form = PokemonFinderForm()
    poke_dict = {}
    if request.method == "POST":
        poke_name = form.name.data

        url = f"https://pokeapi.co/api/v2/pokemon/{poke_name}"
        res = requests.get(url)
        if res.ok:
            data = res.json()
            user_pokemon = []
            poke_dict = {
                'name': data['name'],
                'ability': data['abilities'][0]['ability']['name'],
                'img_url': data['sprites']['front_shiny'],
                'hp': data['stats'][0]['base_stat'],
                'attack': data['stats'][1]['base_stat'],
                'defense': data['stats'][2]['base_stat']
            }
            #pokemon = Pokemon(name, hp, defense, attack, img_url, ability)
            #if pokemon is not in user_pokemon:

            name = data['name']
            ability = data['abilities'][0]['ability']['name']
            img_url = data['sprites']['front_shiny']
            hp = data['stats'][0]['base_stat']
            attack = data['stats'][1]['base_stat']
            defense = data['stats'][2]['base_stat']
            user_pokemon.append(poke_dict)
            pokemon = Pokemon(name, hp, defense, attack, img_url, ability)
            db.session.add(pokemon)
            db.session.commit()


# append searched pokemon into users team

    return render_template('pokemon.html', form=form, pokemon=poke_dict)


##############################################################

@poke.route('/pokemon', methods=['GET'])
@login_required
def user_team():
    team = current_user.team
    return render_template('user_team', team=team)
# catch searched pokemon

# append search? to what? team? upload team?

##############################################################

# find user

# battle

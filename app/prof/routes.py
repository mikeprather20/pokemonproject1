from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import EditProfile
from app.models import User

from app.models import db

prof = Blueprint('prof', __name__, template_folder='profiletemplate')

##########################################################################

@prof.route('/profile')
def userProfile():
    return render_template('profile.html')


##########################################################################


@prof.route('/editprofile', methods = ["GET", "POST"])
def editProfile():
    form = EditProfile()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = form.password.data

            user = User( username, first_name, last_name, email, password)

            db.session.update(user)
            db.session.commit()
            flash("Profile changed.", 'success')
        return redirect(url_for('prof.editProfile'))
    return render_template('editprofile.html', form = form)


##########################################################################
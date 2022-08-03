from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import EditProfile
from app.models import User
from app.models import db
from flask_login import current_user
prof = Blueprint('prof', __name__, template_folder='profiletemplate')

##########################################################################

@prof.route('/profile')
def userProfile():
    return render_template('profile.html')


##########################################################################


@prof.route('/editprofile', methods = ["GET", "POST"])
def editProfile():
    form = EditProfile()
    user = User.query.get(current_user.id)
    if request.method == "POST":
        if form.validate():
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data

            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            db.session.commit()
            flash("Profile changed.", 'success')
        return redirect(url_for('prof.editProfile'))
    return render_template('editprofile.html', form = form,user = user)


##########################################################################
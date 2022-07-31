from flask import Blueprint, render_template


prof = Blueprint('prof', __name__, template_folder='profiletemplates')

@prof.route('/profile')
def userProfile():
    return render_template('profile.html')


##########################################################################


@prof.route('/editprofile')
def editProfile():
    return render_template('editprofile.html')


##########################################################################
from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

    #dear lord please help me with this project
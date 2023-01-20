from flask import Flask, request, render_template, redirect, flash, jsonify
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chickens'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

MOVIES = {'Jurassic Park', 'Pulp Fiction', 'Step Brothers'}

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/old-home-page')
def redirect_to_home():
    '''Redirects to new homepage'''
    flash('That page has moved.  This is the new page.')
    return redirect('/')

@app.route('/movies')
def show_all_movies():
    '''Show list of all movies in fake DB'''
    return render_template('movies.html', movies=MOVIES)

@app.route('/movies/json')
def get_movies_json():
    json_obj = jsonify(list(MOVIES))
    return json_obj 

@app.route('/movies/new', methods=['POST'])
def add_movie():
    
    title = request.form['title']
    # Add to pretend DB
    if title in MOVIES:
        flash('Movie is already in list', 'error')
    else:
        MOVIES.add(title)
        flash('Added Your Movie!', 'success')
    return redirect('/movies')
from app import app
from flask import request
import search_scraper, home_scraper
import json


@app.route('/')
def index():
    return '<h1>This is working!</h1>'

@app.route('/<category>/<name>/<id>', methods=['POST', 'GET'])
def get_songs(category, name, id):
    data = json.dumps(get_songs_from_scraper(category, name, id))
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response

def get_songs_from_scraper(category, name, id):
    url = home_scraper.BASE_URL + '/' + category + '/' + name + '/' + id
    return home_scraper.get_songs(url)

@app.route('/songs', methods=['GET', 'POST'])
def top_songs():
    category = 'songs'
    if(request.method=='POST'):
        count = request.form['count']
        language = request.form['language']
    else:
        count = 5
        language = 'english'
    data = json.dumps(home_scraper.fetch(category, count, language))
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response
 
@app.route('/albums', methods=['GET', 'POST'])
def new_albums():
    category = 'albums'
    if(request.method=='POST'):
        count = request.form['count']
        language = request.form['language']
    else:
        count = 5
        language = 'english'
    data = json.dumps(home_scraper.fetch(category, count, language))
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response
 
@app.route('/playlists', methods=['GET', 'POST'])
def featured_playlists():
    category = 'playlists'
    if(request.method=='POST'):
        count = request.form['count']
        language = request.form['language']
    else:
        count = 5
        language = 'english'
    data = json.dumps(home_scraper.fetch(category, count, language))
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response
 
@app.route('/search/songs', methods=['GET', 'POST'])
def search_songs():
    category = 'songs'
    if(request.method=='POST'):
        count = request.form['count']
        keyword = request.form['key']
    else:
        count = 5
        keyword = "the weeknd"
    data = json.dumps(search_scraper.search(category, count, keyword))
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/search/albums', methods=['GET', 'POST'])
def search_albums():
    category = 'albums'
    if(request.method=='POST'):
        count = request.form['count']
        keyword = request.form['key']
    else:
        count = 5
        keyword = "the weeknd"
    data = json.dumps(search_scraper.search(category, count, keyword))
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/search/playlists', methods=['GET', 'POST'])
def search_playlists():
    category = 'playlists'
    if(request.method=='POST'):
        count = request.form['count']
        keyword = request.form['key']
    else:
        count = 5
        keyword = "the weeknd"
    data = json.dumps(search_scraper.search(category, count, keyword))
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response
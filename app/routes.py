from app import app
from flask import request
import search_scraper, home_scraper
import json


@app.route('/')
def index():
    return '<h1>This is working!</h1>'

# @app.route('/search', methods=['GET', 'POST'])
# def search():
#     if(request.method=='POST'):
#         keyword = request.form['key']
#         category = request.form['category']
#         count = request.form['count']
#     elif(request.method=='GET'):
#         keyword = 'something like that'
#         category = 'song'
#         count = '4'
#     data = json.dumps(search_scraper.search(keyword, category, count))
#     response = app.response_class(
#         response=data,
#         status=200,
#         mimetype='application/json'
#     )
#     return response

# @app.route('/recommendations', methods=['GET', 'POST'])
# def recommend():
#     if(request.method=='POST'):
#         category = request.form['category']
#         count = request.form['count']
#         language = request.form['language']
#     elif(request.method=='GET'):
#         category = "songs"
#         count = '5'
#         language = 'english'
#     data = json.dumps(home_scraper.fetch(category, count, language))
#     response = app.response_class(
#         response=data,
#         status=200,
#         mimetype='application/json'
#     )
#     return response

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
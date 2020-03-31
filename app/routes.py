from app import app
from flask import request
import home_scraper, search_scraper
import json


@app.route('/')
def index():
    return '<h1>This is working!</h1>'

@app.route('/search')
def search():
    keyword = request.form['key']
    category = request.form['category']
    count = request.form['count']
    data = json.dumps(search_scraper.search(keyword, category, count))
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/recommendations')
def recommend():
    # category = request.form['category']
    # count = request.form['count']
    # language = request.form['language']
    category = "songs"
    count = '5'
    language = 'english'
    data = json.dumps(home_scraper.fetch(category, count, language))
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response
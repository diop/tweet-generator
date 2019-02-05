import flask
from app import app
import requests
from flask import render_template

response = requests.get('http://api.open-notify.org/astros.json')
people = response.json()

people = {person['name'] for person in people['people']}

@app.route('/')
def index():
    return render_template('index.html', people=people)

@app.route('/tweet-generator/<name>')
def person(name):
    if name in people:
        return f'{name} might be in space'
    else:
        return f'{name} is on earth'
        
# names = {person['name] for person in people['people]}
# # if any(name == person['name] for person in people):   
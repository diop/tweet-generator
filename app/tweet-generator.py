
# export FLASK_APP=tweet-generator.py
# python -m flask run

import requests 
from app import app
from pprint import pprint

response = requests.get('http://api.open-notify.org/astros.json')

people = response.json()

pprint(people['number'])
from flask import Flask 
import requests
from utilities import *
from indico import *

app = Flask(__name__)

@app.route('/')
def hello():
	return "Welcome to the Slack winning team"

@app.route('/keywords')
def fetch_keywords():
	return ""

@app.route('/categories')
def fetch_categories():
	return ""

@app.route('/emotion')
def fetch_emotion():
	return ""

@app.route('/city/<city>')
def fetch_city_data(city):
	return "this is " + city

if __name__ == "__main__":
	app.run(host='localhost', port=23001, debug=True)

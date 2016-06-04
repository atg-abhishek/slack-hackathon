from flask import Flask 
import requests
from utilities import *

app = Flask(__name__)

@app.route('/')
def hello():
	return "Welcome to the Slack winning team"


if __name__ == "__main__":
	app.run(host='localhost', port=32001, debug=True)

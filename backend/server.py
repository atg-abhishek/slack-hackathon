from flask import Flask
from flask import Markup
from flask import render_template
import requests
from utilities import *
from indico import *
from data_processor import *

app = Flask(__name__)

@app.route('/')
def hello():
	return "Welcome to the Slack winning team"

@app.route("/chart/<city>")
def index(city):
  chartID = 'chart_ID'
  chart_type = 'line'
  chart_height = 350

  chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
  # series = [{"name": 'Label1', "data": [1,2,3]}, {"name": 'Label2', "data": [4, 5, 6]}]
  title = {
            "text": 'Two Week Team Morale',
            "x": -20 #center
        }
  xAxis = {"categories": ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']}
  yAxis = {"title": {"text": 'yAxis Label'},
              "plotLines": [{
                "value": 0,
                "width": 1,
                "color": '#808080'
            }]}
  series = [{
            "name": city.upper(),
            "data": pre_chart_data(city)
        }]
  return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

    # labels = ["January","February","March","April","May","June","July","August"]
    # values = [10,9,8,7,6,4,7,8]
    # return render_template('chart.html', values=values, labels=labels)

@app.route('/keywords')
def fetch_keywords():
	return ""

@app.route('/categories')
def fetch_categories():
	return ""

@app.route('/emotion')
def fetch_emotion():
	return ""

# @app.route('/city/<city>')
# def fetch_city_data(city):
# 	return "this is " + city

@app.route('/trigger')
def trigger():
	x = execute()
	return x

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=23001, debug=True)

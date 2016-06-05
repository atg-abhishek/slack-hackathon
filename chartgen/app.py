from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index(chartID = 'chart_ID', chart_type = 'line', chart_height = 350):
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
            "name": 'Tokyo',
            "data": [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
        }, {
            "name": 'New York',
            "data": [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]
        }, {
            "name": 'Berlin',
            "data": [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0]
        }, {
            "name": 'London',
            "data": [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
        }]
  return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

if __name__ == "__main__":
  app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)
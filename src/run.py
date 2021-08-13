from flask import Flask
from flask import render_template
from flask import jsonify
from utils import get_ft_time

app = Flask(__name__, static_url_path='/static')

@app.route("/info_json")
def info_json():
    dummy_data = [
        {
            "id" : 1,
            "starting_time" : "00:00",
            "team_a" : "Random Team 1",
            "score" : "0 - 0",
            "team_b" : "Random Team 2",
            "minute" : get_ft_time('00:00'),
        },
        {
            "id" : 2,
            "starting_time" : "00:05",
            "team_a" : "Random Team 3",
            "score" : "0 - 0",
            "team_b" : "Random Team 4",
            "minute" : get_ft_time('00:05'),
        },
        {
            "id": 3,
            "starting_time": "00:00",
            "team_a": "Random Team 5",
            "score": "0 - 0",
            "team_b": "Random Team 6 ",
            "minute" : get_ft_time('00:06'),
        },
    ]
    return jsonify(dummy_data)

@app.route("/")
def index():
    matches = info_json()
    return render_template(
        'index.html',
        matches=matches.json
    )
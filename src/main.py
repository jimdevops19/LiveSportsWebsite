from flask import Flask
from flask import render_template, jsonify

app = Flask(__name__)

@app.route('/data_json')
def data_json():
    dummy_data = [
        {
            "id": 1,
            "starting_time": "16:00",
            "team_a": "Random Team 1",
            "score": "1 - 2",
            "team_b": "Random Team 2",
            "minute": "01:00",
        },
        {
            "id": 2,
            "starting_time": "18:00",
            "team_a": "Random Team 3",
            "score": "1 - 1",
            "team_b": "Random Team 4",
            "minute": "05:00",
        },
    ]
    return jsonify(dummy_data)

@app.route('/')
def index():
    dummy_data = data_json()
    return render_template(
        'index.html',
        matches=dummy_data.json,
    )
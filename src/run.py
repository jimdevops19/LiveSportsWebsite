from flask import Flask
from flask import render_template
from flask import jsonify
from utils import get_ft_time
import json

app = Flask(__name__, static_url_path='/static')

@app.route("/info_json")
def info_json():
    with open('dummy_data.json', 'r') as f:
        dummy_data = json.load(f)

    # Overrides:
    for item in dummy_data:
        if item.get('minute') == '':
            item['minute'] = get_ft_time(item.get('starting_time'))


    return jsonify(dummy_data)

@app.route("/")
def index():
    matches = info_json()
    return render_template(
        'index.html',
        matches=matches.json
    )
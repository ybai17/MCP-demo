# This file contains the main server application for handling horse and race data requests

from flask import Flask, jsonify
from init_data import init_horses, init_races
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

logger.info("Starting main server...")

app = Flask(__name__)
horses = init_horses()
races = init_races()

logger.info("Initialized horses and races")
logger.info(f"Horses: {horses}")
logger.info(f"Races: {races}")

@app.route('/', methods=['GET'])
def home():
    return jsonify(message="Hello, World!")

@app.route('/horse/', methods=['GET'])
def list_horses():
    return jsonify({'data': list(horses.keys())})

@app.route('/race/', methods=['GET'])
def list_races():
    return jsonify({'data': list(races.keys())})

@app.route('/horse/<string:name>', methods=['GET'])
def disp(name):
    try:
        return jsonify({'data': horses[name]})
    except KeyError:
        return jsonify({'error': 'Horse not found'}), 404

@app.route('/horse/<string:name>/color', methods=['GET'])
def disp_color(name):
    try:
        return jsonify({'data': horses[name].get('color')})
    except KeyError:
        return jsonify({'error': 'Horse not found'}), 404

@app.route('/race/<string:name>', methods=['GET'])
def disp_race(name):
    try:
        return jsonify({'data': races[name]})
    except KeyError:
        return jsonify({'error': 'Race not found'}), 404

logger.info("Server is running")

if __name__ == '__main__':
    app.run(debug=True)

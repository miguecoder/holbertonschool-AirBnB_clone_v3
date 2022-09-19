#!/usr/bin/python3
"""Python script that give Status of API"""

from os import getenv
from models import storage
from flask import Flask
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def storageclose(error):
    """Method that close the storage in teardown"""
    storage.close()


@app.errorhandler(404)
def page_404(e):
    """ Method to handle 404 status code response """
    return ({'error': 'Not found'}), 404


if __name__ == '__main__':
    HBNB_API_HOST = getenv('HBNB_API_HOST')
    HBNB_API_PORT = getenv('HBNB_API_PORT')
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)

#!/usr/bin/python3
"""Python script that give Status of API"""

from models import storage
from flask import Flask, Blueprint
from api.v1.views import app_views
from api.v1.views.index import index_views

app = Flask(__name__)
app.register_blueprint(app_views)
app.register_blueprint(index_views)


@app.teardown_appcontext
def storageclose(error):
    """Method that close the storage in teardown"""
    storage.close()


@app.errorhandler(404)
def page_404(e):
    """ Method to handle 404 status code response """
    return ({'error': 'Not found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', threaded=True)

#!/usr/bin/python3
"""Python script that give Status of API"""

from api.v1.views import app_views
from flask import jsonify, Blueprint
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

index_views = Blueprint('index_views', __name__,
                        template_folder='views',
                        url_prefix='/api/v1/')


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def Status():
    """returns a json with the status"""
    return jsonify({"status": "OK"})


@index_views.route('/stats', methods=['GET'], strict_slashes=False)
def counter():
    """retrieves the number of each objects by type"""
    dict_return = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }

    return jsonify(dict_return)

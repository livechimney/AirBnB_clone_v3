#!/usr/bin/python3
<<<<<<< HEAD
"""
app
"""

from flask import Flask, jsonify
from flask_cors import CORS
from os import getenv

from api.v1.views import app_views
from models import storage


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

=======
'''
    app for registering blueprint and starting flask
'''
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
CORS(app, origins="0.0.0.0")
>>>>>>> a75d183d98c819783e74a236d2eb41bd63ef1748
app.register_blueprint(app_views)


@app.teardown_appcontext
<<<<<<< HEAD
def teardown(exception):
    """
    teardown function
    """
=======
def tear_down(self):
    '''
    close query after each session
    '''
>>>>>>> a75d183d98c819783e74a236d2eb41bd63ef1748
    storage.close()


@app.errorhandler(404)
<<<<<<< HEAD
def handle_404(exception):
    """
    handles 404 error
    :return: returns 404 json
    """
    data = {
        "error": "Not found"
    }

    resp = jsonify(data)
    resp.status_code = 404

    return(resp)

if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"))
=======
def not_found(error):
    '''
    return JSON formatted 404 status code response
    '''
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST", "0.0.0.0"),
            port=int(getenv("HBNB_API_PORT", "5000")), threaded=True)
>>>>>>> a75d183d98c819783e74a236d2eb41bd63ef1748

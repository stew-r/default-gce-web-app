import logging
from flask import Flask
import requests 


app = Flask(__name__)


def get_zone():
    host = 'metadata.google.internal'
    path = 'computeMetadata/v1/instance/zone'
    url = f'http://{host}/{path}'
    headers = {'Metadata-Flavor': 'Google'}
    r = requests.get(url=url, headers=headers)
    zone = r.text.split('/')[-1]
    return r.text


@app.route('/')
def hello_world():
    app.logger.info('this is an INFO message')
    try:
        return get_zone()
    except Exception as e:
        app.logger.error(e)
        return "Unable to generate a valid response. Are you sure you're " +\
            "running on Google Compute Engine?\n"


# Sets Flask application logger’s handlers to match Gunicorn’s
# https://medium.com/@trstringer/logging-flask-and-gunicorn-the-manageable-way-2e6f0b8beb2f
if __name__ != "__main__":
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


# Starts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0")
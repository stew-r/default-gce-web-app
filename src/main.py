from flask import Flask
import requests 

app = Flask(__name__)

def get_zone():
    host = 'metadata.google.internal'
    path = 'computeMetadata/v1/instance/zone'
    url = f'{host}/{path}'
    headers = {'Metadata-Flavor': 'Google'}
    r = requests.get(url=url, headers=headers)
    zone = r.text.split('/')[-1]
    return r.text


@app.route('/')
def hello_world():
    try:
        return get_zone()
    except Exception as e:
        return "Unable to generate a valid response. Are you sure you're " +\
            "running on Google Compute Engine?"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
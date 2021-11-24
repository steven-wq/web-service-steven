import os, json, random
from flask import Flask, jsonify, make_response, request
from http.client import HTTPException
from urllib.error import HTTPError, URLError

app = Flask(__name__)
log = app.logger

@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'XEFI: Formation WebService')
    return 'Welcome to {}!\n'.format(target)

@app.route('/webservice', methods=['GET', 'POST'])
def webservice():

    # Get request parameters
    req = request.args

    message = req['message']
    key = req['key']

    # Write an algorithm to encrypt the message with the key
    crypted = 'your encrypted message'

    data = {'message': message, 'key': key, 'crypted': crypted}

    return data


if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
pp.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    return 'Hello HBNB'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

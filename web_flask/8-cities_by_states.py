#!/usr/bin/python3
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


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


@app.route('/python')
@app.route('/python/<text>')
def python_is_fun(text='is cool'):
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>')
def isanumber(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n=None):
    return render_template('6-number_odd_or_even.html', n=n)


@app.teardown_appcontext
def teardown_app(exception):
    storage.close()


@app.route('/states_list')
def states_list():
    states = []
    for key, values in storage.all('State').items():
        states.append(values)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def cities_by_states():
    states = storage.all("State")
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

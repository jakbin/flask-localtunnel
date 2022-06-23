# flask-localtunnel

 [![PyPI version](https://badge.fury.io/py/flask-localtunnel.svg)](https://badge.fury.io/py/flask-localtunnel)
 [![Downloads](https://pepy.tech/badge/flask-localtunnel/month)](https://pepy.tech/project/flask-localtunnel)
 [![Downloads](https://static.pepy.tech/personalized-badge/flask-localtunnel?period=total&units=international_system&left_color=green&right_color=blue&left_text=Total%20Downloads)](https://pepy.tech/project/flask-localtunnel)
 ![Python 3.6](https://img.shields.io/badge/python-3.6-yellow.svg)

### This inspired from flask-ngrok


### Disclaimer:-
Use it only for educational purpose.


A simple way to demo Flask apps from your machine.
Makes your [Flask](http://flask.pocoo.org/) apps running on localhost available
 over the internet via the excellent [localtunnel](https://github.com/localtunnel/localtunnel) tool.

## Compatability
Python 3.6+ is required.

## Installation

```bash
pip install flask-localtunnel
```
### Inside Jupyter / Colab Notebooks

```bash
!pip install flask
```

## Quickstart
1. Import with ```from flask_localtunnel import run_with_lt```
2. Add `run_with_lt(app)` to make your Flask app available upon running
```python
# flask_ngrok_example.py
from flask import Flask
from flask_lt import run_with_lt

app = Flask(__name__)
run_with_lt(app)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
```
Running the example:
```bash
python flask_lt_example.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * localtunnel is alreadty installed.
 * your url is: https://<random-url>.loca.lt
```

### Contributer :- 
- @henk717
- @NobreHD : subdomain support 

from flask import Flask
from flask_lt import run_with_lt

app = Flask(__name__)
run_with_lt(app)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()

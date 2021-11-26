from flask import Flask 
from flask_lt import run_with_lt

app = Flask(__name__)
run_with_lt(app)
app.secret_key = 'super-secret-key'

@app.route("/")
def home():
    return "localtunnel is working."
    
if __name__ == "__main__":
    app.run()    

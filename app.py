import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World from flask app!"

@app.route('/time')
def time_display():
    return "Current date, time : "+datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Default to 8000 for Azure
    app.run(host="0.0.0.0", port=port)

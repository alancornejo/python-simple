import os
from flask import Flask
app = Flask(__name__)

name = os.environ['nombre']

@app.route("/")
def hello():
    return f"Hello World mi nombre es : {name}!"
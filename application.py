import os
from flask import Flask
app = Flask(__name__)

from dotenv import load_dotenv
load_dotenv()
name = os.getenv("nombre", 8081)

@app.route("/")
def hello():
    return f"Hello World mi nombre es : {name}!"
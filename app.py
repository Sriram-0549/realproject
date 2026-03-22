from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/api")
def home():
    name = request.args.get("name", "Guest")
    message = os.getenv("MESSAGE", "Welcome")
    return f"{message}, {name}!"

app.run(host="0.0.0.0", port=5000)

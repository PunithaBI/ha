# app.py

from flask import Flask
import os

app = Flask(__name__)

# Home route
@app.route("/")
def hello_world():
    return "Hello, World from Azure App Service!"

# Health check route
@app.route("/healthcheck")
def healthcheck():
    return "Healthy", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

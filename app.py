import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello welcome to Crane Cloud Docs Sample Flask API"

@app.route('/about')
def about():
    return "This is the about-route for this sample API"

@app.route('/support')
def support():
    return "This is the support-route for this sample API"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True,host='0.0.0.0',port=port)
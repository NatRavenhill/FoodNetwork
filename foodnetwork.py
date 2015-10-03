from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/foodbank")
def foodbank():
    return render_template('foodbank.html')

@app.route("/donator")
def donator():
    return render_template('donator.html')

@app.route("/receiver")
def receiver():
    return render_template('receiver.html')

if __name__ == "__main__":
    app.debug = True
    app.run()

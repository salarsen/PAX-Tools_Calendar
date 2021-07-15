from logging import debug
from flask import Flask
from flask import render_template

application = Flask(__name__)

@application.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    application.debug=False
    application.run()
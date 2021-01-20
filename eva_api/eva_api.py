from flask import Flask

application = Flask(__name__)


@application.route("/")
def index():
    return "Hello uWSGI from python version: <br>"


if __name__ == '__main__':
    application.run()

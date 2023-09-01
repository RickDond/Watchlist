import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient

from wl.routes import pages

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    mc = MongoClient(os.environ.get("MONGODBURI"))
    app.db = mc.watchlist

    app.register_blueprint(pages)
    return app
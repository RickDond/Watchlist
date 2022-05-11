import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient

from wl.routes import pages

load_dotenv()


def create_app():
    app = Flask(__name__)
    #app.config["MONGODB_URI"] = os.environ.get("MONGODB_URI")
    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", "d3a5b151-4fd9-427d-9852-5107d0e9f69f"
    )
    #app.db = MongoClient(app.config["MONGODB_URI"]).get_default_database()

    mc = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = mc.watchlist
    #content = app.db["watch_collection"]


    app.register_blueprint(pages)
    return app
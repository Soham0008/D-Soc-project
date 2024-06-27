import os
import psycopg2
from flask import Flask
from .InventoryItem import InventoryItem
from .Customer import Customer
from .Staff import Staff
from .Transaction import Transaction

def create_app(test_config=None):
    # Create & configure app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='postgresql://soham:1234@localhost/Pos',
    )

    # Ensuring instance folder exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # simple page saying hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app

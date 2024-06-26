from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app: Flask = Flask(__name__)
CORS(app)  # allows for cross-origin requests

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db: SQLAlchemy = SQLAlchemy(app)
from flask import Flask, request, jsonify
from config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
server = Flask(__name__)
server.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(server, db)
from app import routes, models
if __name__ == '__main__':
  server.run()

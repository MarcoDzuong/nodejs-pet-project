from flask import Flask, request, jsonify
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.config.from_object(Config)
from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# from app import  models
if __name__ == '__main__':
    app.run(threaded=True, port=5000)

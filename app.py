from flask import Flask
from flask_cors import CORS
from app.auth.route.customer_route import customer_bp
from app.auth.route.establishment_route import establishment_bp
from app.auth.route.review_route import review_bp
from flasgger import Swagger
import os
from dotenv import load_dotenv

from app import db

load_dotenv()

app = Flask(__name__)
CORS(app)
Swagger(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'false').lower() == 'true'

db.init_app(app)

app.register_blueprint(customer_bp, url_prefix='/api')
app.register_blueprint(establishment_bp, url_prefix='/api')
app.register_blueprint(review_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

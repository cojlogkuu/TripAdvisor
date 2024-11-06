from flask import Flask
from flask_cors import CORS
from yaml import safe_load
from app.auth.route.customer_route import customer_bp
from app.auth.route.establishment_route import establishment_bp
from app.auth.route.review_route import review_bp

from app import db

app = Flask(__name__)

CORS(app)

with open('config/app.yml', 'r') as file:
    config = safe_load(file)

app.config['SQLALCHEMY_DATABASE_URI'] = config['database']['uri']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['database']['track_modifications']

db.init_app(app)

app.register_blueprint(customer_bp, url_prefix='/api')
app.register_blueprint(establishment_bp, url_prefix='/api')
app.register_blueprint(review_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from urllib.parse import quote

project_path = "C:\\Learning\\Python Projects\\restaurant_management"  # Configure here project path

db_config = {"user": "postgres",
             "password": "*****",  # add password for the database connection
             "db": "postgres",
             "host": "****",  # add host info
             "port": 5432,
             "schema": "public",
             "table": "restaurant"}

db_url = f'''postgresql+psycopg2://{db_config["user"]}:{quote(db_config["password"])}@{db_config["host"]}:{db_config["port"]}/{db_config["db"]}'''

# creating an instance of the flask app
app = Flask(__name__)

# Configure our Database
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

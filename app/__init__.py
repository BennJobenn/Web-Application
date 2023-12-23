from flask import Flask
from flask_mysql_connector import MySQL
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL, CLOUD_NAME, API_KEY, API_SECRET
import cloudinary
import os
mysql = MySQL()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY =SECRET_KEY,
        MYSQL_USER= DB_USERNAME,
        MYSQL_PASSWORD = DB_PASSWORD,
        MYSQL_DATABASE = DB_NAME,
        MYSQL_HOST = DB_HOST,
        #BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
    )
    mysql.init_app(app)

    cloudinary.config(
        cloud_name= CLOUD_NAME,
        api_key= API_KEY,
        api_secret=API_SECRET,
    )


    from app.routes.studentroute import studentroute
    app.register_blueprint(studentroute)

    from app.routes.courseroute import courseroute
    app.register_blueprint(courseroute)

    from app.routes.collegeroute import collegeroute
    app.register_blueprint(collegeroute)

    return app

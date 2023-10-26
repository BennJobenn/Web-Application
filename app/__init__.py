from flask import Flask
from flask_mysql_connector import MySQL
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL

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


    from app.routes.studentroute import studentroute
    app.register_blueprint(studentroute)

    from app.routes.courseroute import courseroute
    app.register_blueprint(courseroute)

    from app.routes.collegeroute import collegeroute
    app.register_blueprint(collegeroute)

    return app


from flask import Flask #import Flask from flask module

from .config import Config #import Config class from config module

from .routes import employees_bp # import employee_db class from routes module

from .db_instance import db # import the db instance from the db_instance


def create_app():
    # create an instance of the Flask application
    app=Flask(__name__)
    
    app.config.from_object(Config)
    
    # intialize the database with the Flask app instance
    db.init_app(app)

    
    app.register_blueprint(employees_bp, url_prefix='/api')


    return app # return the Flask app instance 

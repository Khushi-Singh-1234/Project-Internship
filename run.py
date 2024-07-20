
# import the create_app function from the app module 
from app.app import create_app 

# import db instance from the db_instance module
from app.db_instance import db

app=create_app() #create an instance of the Flask application

if __name__=='__main__': 
    with app.app_context():
        # create all the database tables
        db.create_all()

    # run the application in debug mode    
    app.run(debug=True)

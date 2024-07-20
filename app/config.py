
import os # import the os module 

base_dir=os.path.abspath(os.path.dirname(__file__)) #get path of the directory where this file is located 

class Config:
    # retrieve the secret key from the environment variables
    SECRET_KEY=os.environ.get('SECRET_KEY')

    # define the database URI for SQLAlchemy to use SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(base_dir, 'employees.db')

    # Disable the modification tracking feature of SQLAlchemy
    sQLALCHEMY_TRACK_MODIFICATIONS= False
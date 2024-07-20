from .db_instance import db  # Import the db instance from the db_instance module

# Define the Employee model, inheriting from db.Model
class Employee(db.Model):

    
    # Define the columns of the employees table
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer,nullable=False)


    # Method to convert the model instance to a dictionary
    def to_dict(self):
        return {
               "id":self.id,
               "name":self.name,
               "department":self.department,
               "age":self.age
            }

    def __repr__(self):
        return f'<Employee {self.name}>'
    
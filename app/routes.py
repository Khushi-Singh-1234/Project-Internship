
# importing Blueprint,request,jsonify,abort classes from flask package
from flask import Blueprint,request,jsonify,abort

# importing EmployeeSchema class from schemas file
from .schemas import EmployeeSchema

# importing Employee class from models file
from .models import Employee

# importing db object from db_instance file
from .db_instance import db


# creating a blueprint route
employees_bp=Blueprint('employees_bp', __name__)

employee_schema=EmployeeSchema()


# welcome statement in web browser
@employees_bp.route('/',methods=['GET'])

def index():
    return ({"message":"Welcome to the Employee Management System !"})


#create an employee to add to database
@employees_bp.route('/employees',methods=['POST']) # decorator line

def create_Employee():

    data=request.get_json() # fecthing data
    
    errors=employee_schema.validate(data) # validating error

    if errors:
        return jsonify(errors),400
    
    new_Employee=Employee(name=data['name'], department=data['department'], age=data['age']) # assing data to value

    db.session.add(new_Employee) # adding values to database

    db.session.commit() # commiting the data

    return "Employee created successfully",201 # output displayed on url

# getting data from database
@employees_bp.route('/employees',methods=['GET'])

def get_all_Employee():

    employee=Employee.query.all()

    return ({"employee":[emp.to_dict()for emp in employee]}) # returning all data from database to url
    


# reading an employee from database by ID
@employees_bp.route('/employees/<int:id>',methods=['GET'])

def get_Employee(id):

    employee=Employee.query.all()

    if not employee:
        abort(404, description= f"Employee with id {id} not found!") 

    return ([{
        'id':emp.id,
        'department':emp.department,
        'age':emp.age,
        'name':emp.name
        } for emp in employee if emp.id==id]) #returning data for single employee for given id of url


                   

# updating details of existing employee
@employees_bp.route('/employees/<int:id>',methods=['PUT'])

def update_Employee(id):

    data=request.get_json(id)

    errors=employee_schema.validate(data)

    if errors:
        return jsonify(errors),400
    
    employee= Employee.query.get_or_404(id)
    
    if not employee:
        return jsonify({"message":'employee not found'}),404
    
    employee.name=data['name']
    employee.department=data['department']
    employee.age=data['age']

    db.session.commit()

    return ({
        'id':employee.id,
        'department':employee.department,
        'age':employee.age,
        'name':employee.name
        } ) # updating the data for given employee id in url
    
    


# route for deleting an employee
@employees_bp.route('/employees/<int:id>',methods=['DELETE'])

def delete_Employee(id):

    employee=Employee.query.get_or_404(id)

    db.session.delete(employee)

    db.session.commit()

    return ({'message':'employee deleted successfully'})


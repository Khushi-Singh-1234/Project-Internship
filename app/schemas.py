from marshmallow import Schema,fields,validate # Import Schema, fields, and validate from the marshmallow module

# Define a schema for the Employee model  
class EmployeeSchema(Schema):
    
    name=fields.Str(Validate=validate.Length(min=1),required=True)

    department=fields.Str(Validate=validate.Length(min=1),required=True)
    
    age=fields.Int(Validate=validate.Length(min=1),required=True)

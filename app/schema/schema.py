""" 
- schema for data validation
"""
class Validate():
    
    _schema_dw = {
        "type": "object",
        "properties": {
            "first_name": {"type": "string",
                     "minLength":2,
                     "maxLength": 50},
            "last_name": {"type": "string",
                     "minLength":2,
                     "maxLength": 50},
            "company_name": {"type": "string",
                     "minLength":2,
                     "maxLength": 50},
            "address": {"type": "string",
                     "minLength":2,
                     "maxLength": 50},
            "city": {"type": "string",
                     "minLength":2,
                     "maxLength": 50},
            "state": {"type": "string",
                     "minLength":2,
                     "maxLength": 2},
            "zip": {"type": "number"},
            "phone1": {"type": "string",
                     "minLength":2,
                     "maxLength": 20},
            "phone2": {"type": "string",
                     "minLength":2,
                     "maxLength": 20},
            "email": {"type": "string",
                     "minLength":2,
                     "maxLength": 50},
            "department": {"type": "string",
                     "minLength":2,
                     "maxLength": 50},
            },
        "required": ["first_name","last_name","email","phone1"]
    }
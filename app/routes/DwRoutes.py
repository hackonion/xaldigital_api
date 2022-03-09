"""
 - API endpoints for REST requests and responses
"""

from flask import Blueprint, jsonify, make_response, request
from model.DwModel import Dw, db
from schema.schema import Validate
from flask_expects_json import expects_json

api = Blueprint('api', __name__)

#Get all items
#Create new item 
@api.route('/get_items',  methods=('GET', 'POST'))
@expects_json(Validate._schema_dw, ignore_for=['GET'])
def get_all_data():
    try:
        dw_item = Dw.query.all()
        if request.method == 'GET':
            return make_response(jsonify(dw_item),200)
        elif request.method == 'POST':
            data = request.get_json()
            item = Dw(
                    first_name = data['first_name'],
                    last_name = data['last_name'],
                    company_name = data['company_name'],
                    address = data['address'],
                    city = data['city'],
                    state = data['state'],
                    zip = data['zip'],
                    phone1 = data['phone1'],
                    phone2 = data['phone2'],
                    email = data['email'],
                    department = data['department'])
            db.session.add(item)     
            db.session.commit()
            return make_response(jsonify("Item create"),201)
    except Exception:
        return make_response(jsonify("Error on the server"),500)
    
#Get item by id
#Update item by id
@api.route('/get_item_by/<int:id>', methods=('GET', 'PUT', 'DELETE'))
@expects_json(Validate._schema_dw, ignore_for=['GET','DELETE'])
def get_item_by(id):
    try:
        dw_item = Dw.query.get(id)
        if request.method  == 'GET':
            return make_response(jsonify(dw_item),200)

        elif request.method == 'PUT':
            data = request.get_json()
            dw_item.first_name = data['first_name']
            dw_item.last_name = data['last_name']
            dw_item.company_name = data['company_name']
            dw_item.address = data['address']
            dw_item.city = data['city']
            dw_item.state = data['state']
            dw_item.zip = data['zip']
            dw_item.phone1 = data['phone1']
            dw_item.phone2 = data['phone2']
            dw_item.email = data['email']
            dw_item.department = data['department']
            
            db.session.add(dw_item)     
            db.session.commit()
            
            return make_response(jsonify(dw_item),200)
        
        elif request.method == 'DELETE':
            db.session.delete(dw_item)
            db.session.commit()
            return make_response(jsonify(dw_item,"Item delete"),200)
        
    except Exception:
        
        return make_response(jsonify("Error on the server"),500)
        
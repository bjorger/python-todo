from flask import Flask, jsonify, Response, request, Blueprint
from api.model.todo import TodoModel
from api.service.todo import TodoService
from api.schema.todo import TodoSchema
from dotenv import load_dotenv

import json

load_dotenv()

app = Flask(__name__)

URL_PREFIX='/v1/todo'

service = TodoService()

@app.route('{}/<string:id>'.format(URL_PREFIX), methods=['GET'])
def get_item(id) -> TodoModel:
    try:
        item = service.get_item(id)
        return Response(item.to_json(), mimetype='application/json'), 200
    except:
        return jsonify({'error': 'There was an error loading the To-Do object'}), 404
    
@app.route('{}/'.format(URL_PREFIX), methods=['GET'])
def get_items():
    print("Get_users")
    try:
        items = service.get_items()
        return Response(json.dumps(items), mimetype='application/json'), 200
    except:
        return jsonify({'There was an error loading the To-Do objects.'}), 400

@app.route('{}/'.format(URL_PREFIX), methods=['POST'])
def create_item():
    try:
        data = request.get_json()
        item = TodoSchema(data['title'], data['description'])
        service.create_item(item)

        return jsonify({'message': 'To-Do created successfully.'}), 200
    except:
        return jsonify({'error': 'There was an error while creating the To-Do object.'}), 400
    
@app.route('{}/<string:id>'.format(URL_PREFIX), methods=['PUT'])
def update_item(id):
    try:
        data = request.get_json()
        if not data['title'] and not data['description']:
            raise Exception()

        service.update_item(id , data['title'], data['description'])
         
        return jsonify({'message': 'To-Do updated successfully.'}), 200
    except:
        return jsonify({'error': 'There was an error while updating the To-Do object.'}), 400
    
@app.route('{}/<string:id>'.format(URL_PREFIX), methods=['DELETE'])
def delete_item(id):
    try:
        service.delete_item(id)
         
        return jsonify({'message': 'To-Do object deleted successfully.'}), 200
    except:
        return jsonify({'error': 'There has been an error while deleting the To-Do object.'}), 400
from flask import Flask, jsonify, make_response, request, Blueprint
from api.model.todo import TodoModel
from api.schema.todo import TodoSchema
from api.service.todo import TodoService
import json

app = Flask(__name__)

URL_PREFIX='/v1/todo'

service = TodoService()

@app.route('{}/'.format(URL_PREFIX))
def get_items():
    print("Get_users")
    try:
        result = service.get_items()
        return jsonify({'res': 'test'})
    except:
        return jsonify({'Internal Server Error'}), 500

@app.route('{}/<string:id>'.format(URL_PREFIX))
def get_item(id) -> TodoModel:
    try:
        item = service.get_item(id)
        return item
    except:
        return jsonify({'error': 'Could not find item with provided id: {}'.format(id)}), 404

@app.route('{}/'.format(URL_PREFIX), methods=['PUT'])
def create_item():
    data = request.get_json()
    print(data)
    
    return jsonify()
    """
    item = Todo
    user_id = request.json.get('userId')
    name = request.json.get('name')
    if not user_id or not name:
        return jsonify({'error': 'Please provide both "userId" and "name"'}), 400

    table.put_item(
        TableName=TODO_TABLE, Item={'userId': {'S': user_id}, 'name': {'S': name}}
    )

    return jsonify({'userId': user_id, 'name': name})
    """
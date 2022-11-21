from api.model.todo import TodoModel
from api.schema.todo import TodoSchema
from typing import List

import uuid
import json
class TodoService: 
    Model: TodoModel
    def __init__(self) -> None:
        if not TodoModel.exists():
            print("Table does not exist")
            TodoModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
        
        
    def get_item(self, id) -> TodoModel:
        try:
            item = TodoModel.get(id)
            return item
        except:
            raise Exception('Could not find item with provided id: {}'.format(id))
    
    def get_items(self) -> List[TodoModel]:
        try:
            items = TodoModel.scan()
            list = []
            
            for item in items:
                list.append({
                    "id": item.id,
                    "title": item.title,
                    "description": item.description
                })
            
            return list
        except:
            print('Something went wrong while scanning table: {}'.format(self.tableName))
            
    def create_item(self, item: TodoSchema) -> None:
        try:
            id = str(uuid.uuid4())
            todo = TodoModel(id=id, title=item.title, description=item.description)
            todo.save()
            print("Successfully created item with ID: {}".format(id))
        except:
            raise Exception('Error while creating Todo Item')
        
    def update_item(self, id: str, title: str, description: str) -> TodoModel:
        try:
            item = TodoModel.get(id)

            item.update(
                actions=[
                    TodoModel.title.set(title),
                    TodoModel.description.set(description)
                ]
            )
        
            return item
        except:
            raise Exception('Could not find item with provided id: {}'.format(id))

    def delete_item(self, id: str) -> TodoModel:
        try:
            item = TodoModel.get(id)
            item.delete()
        except:
            raise Exception('Could not delete item with provided id: {}'.format(id))
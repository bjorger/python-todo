import boto3 
from api.model.todo import TodoModel
from api.schema.todo import TodoSchema
from typing import List

class TodoService:  
    def __init__(self) -> None:
        if not TodoModel.exists():
            print("Table does not exist")
            TodoModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
        
    def get_item(self, id) -> TodoModel:
        result = self.table.get_item(Key={'id': {'S': id}})
        item = result.get('Item')
        if not item:
            raise Exception('No item with id: {} found'.format(id))

        return item
    
    def get_items(self) -> List[TodoModel]:
        try:
            print("Scanning Table for items")
            items = self.table.scan()
        
            if not items:
                return []
            
            return items
        except:
            print('Something went wrong while scanning table: {}'.format(self.tableName))
            
    def create_item(self, item: TodoSchema) -> str:
        print(item.title)
        print(item.description)
        todo = TodoModel(item.title, item.description)
        print(todo)
        return ""
        """
        print(todo)
        try:
            print("Hallo")
            todo = TodoModel(item.title, item.description)
            print(todo)
            todo.save()
        
        """
        """
            uuid = str(uuid.uuid4())
            self.table.put_item(
                Item={
                    id: uuid,
                    'title': item.title,
                    'description': item.description
                }
            )
        """
        """
            return 0
        except:
            raise Exception('Error while creating Todo Item')
        """
        

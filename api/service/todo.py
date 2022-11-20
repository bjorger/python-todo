import boto3 
from api.model.todo import TodoModel
from api.schema.todo import TodoSchema
from typing import List

class TodoService:
    table: any
    tableName = 'TODO_TABLE'
    
    def __init__(self) -> None:
        print("Initializing Todo Service")
        self.table = boto3.resource('dynamodb').Table('TODO_TABLE')
        print("Successfully initialized Todo Service")
        
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
        try:
            uuid = str(uuid.uuid4())
            self.table.put_item(
                Item={
                    id: uuid,
                    'title': item.title,
                    'description': item.description
                }
            )
            
            return uuid
        except:
            raise Exception('Error while creating Todo Item')
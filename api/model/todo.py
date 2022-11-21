from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from dotenv import load_dotenv
import os

class TodoModel(Model):
    class Meta:
        table_name = 'TODO_TABLE'
        aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
        aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
        
    title = UnicodeAttribute(hash_key=True)
    description = UnicodeAttribute()
    
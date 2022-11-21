from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

import os

class TodoModel(Model):
    """
        A To Do Item
    """
    class Meta:
        table_name = 'TODO_TABLE'
        aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
        aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    id = UnicodeAttribute(hash_key=True)
    title = UnicodeAttribute()
    description = UnicodeAttribute()
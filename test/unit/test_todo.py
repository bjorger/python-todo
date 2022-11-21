from api.model.todo import TodoModel
from api.main import app
import pytest
import uuid

def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
    id = str(uuid.uuid4())
    item = TodoModel(id, title='Title', description='Description')
    assert item.id == id
    assert item.title == 'Title'
    assert item.description == 'Description'


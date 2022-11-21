from fixture.app_fixture import client
    
def test_request_example(client):
    response = client.get("/v1/todo/")
    assert b"<h2>Hello, World!</h2>" in response.data
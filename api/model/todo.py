class TodoModel:
    id: str
    title: str
    description: str
    
    def __init__(self, id, title, description) -> None:
        self.id(id)
        self.title(title)
        self.description(description)
    
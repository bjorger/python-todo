class TodoSchema:
    title: str
    description: str
    
    def __init__(self, title, description) -> None:
        self.title = title
        self.description = description
class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return F"Item: {self.name} Description: {self.description}"

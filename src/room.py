# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items  # object

    def __str__(self):
        message = F"{self.name}**"
        message += F"\n Description: {self.description}"
        message += F"\n Items available in the room: {self.items}"
        return(message)

    def room_direction(self, direction):
        if hasattr(self, F"{direction}_to"):
            return getattr(self, F"{direction}_to")
        return None

    def add_item_to_room(self, item):
        self.items.append(item)
        print(F"{item.name} has been added to {self.name}")

    def remove_item_from_room(self, item):
        self.items.remove(item)
        print(F"{item.name} has been removed from {self.name}")

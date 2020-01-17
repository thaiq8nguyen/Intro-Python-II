# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room  # object
        self.inventory = []

    def take_item(self, item_name):
        for item in self.current_room.items:
            if item.name == item_name:
                self.inventory.append(item)
                self.current_room.remove_item_from_room(item)
                print(F"You have picked up a {item_name}")
            else:
                print(F"{item_name} is not found in {self.current_room.name}")

    def drop_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.inventory.remove(item)
                self.current_room.add_item_to_room(item)
                print(F"You have dropped a {item_name}")
            else:
                print(F"{item_name} is not found in your inventory")

    def get_inventory(self):
        return self.inventory

    def travel(self, direction):
        next_room = self.current_room.room_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("There is no room in that direction")

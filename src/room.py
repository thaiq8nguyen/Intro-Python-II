# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return(F"Room: {self.name} \n Description: {self.description}")

    def room_direction(self, direction):
        if hasattr(self, F"{direction}_to"):
            return getattr(self, F"{direction}_to")
        return None

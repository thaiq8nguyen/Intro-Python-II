
from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("sword", "weapon"), Item("rock", "utility")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("key", "utility"), Item("armour", "clothing")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("sword", "weapon"), Item("coin", "currency")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("bow", "weapon"), Item("quiver", "container")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("arrows", "weapon"), Item("potion", "enhancement")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("Please enter your name: ")
player = Player(player_name, room["outside"])
print(F"You are at the {player.current_room}")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


verbs = ["n", "s", "e", "w"]
while True:
    cwd = input("Action: ").lower()

    command = cwd.split()

    if len(command) == 1 and command[0] in verbs:

        player.travel(command[0])
    elif len(command) == 2 and command[0] == "take":
        item = command[1]
        player.take_item(item)

    elif len(command) == 2 and command[0] == "drop":
        item = command[1]
        player.drop_item(item)

    elif command[0] == "i":
        print(F"Your current inventory ~> {player.get_inventory()}")

    elif command[0] == "q":
        exit()
        break

    else:
        print("Please enter a valid command or 'q' to quit the game")

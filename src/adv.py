from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["sword", "shield"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["skull", "torch"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["rope", "potion"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["knife", "apple"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["cobwebs"]),
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
newPlayer = Player("Matt", room['outside'])
CRED = '\033[91m'
CEND = '\033[0m'
print(CRED + str(newPlayer) + CEND)


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
player_input = None
while (player_input is not 'q'):
    print(f'''You are in the {newPlayer.current_room.room_name}:\n
    '{newPlayer.current_room.room_description}. You are holding {newPlayer.items}.'
    You notice the following items:{newPlayer.current_room.items}.\n
    Please pick a direction to move in (n, e, s, w). Interested in items? Need to clean out your bag? Use 'take' to add to your inventory, or 'drop' to clear your inventory.\n''')
    player_input = input("Enter your action: ")
    previous_room = newPlayer.current_room
    if player_input != 'take' and player_input != 'drop':
        newPlayer.move(player_input)
    if player_input.startswith('take '):
        items = player_input.split(' ')
        newPlayer.pickup(items[1])
    if player_input.startswith('drop '):
        items = player_input.split(' ')
        newPlayer.drop(items[1])
    # elif player_input == 'take':
        #player_input = input('What do you choose to take? ')
        # newPlayer.pickup(player_input)
    # elif player_input == 'drop':
        #player_input = input('What do you no longer need? ')
        # newPlayer.drop(player_input)
    if newPlayer.current_room == None:
        print("********You are blocked by a mysterious force.********")
        newPlayer.current_room = previous_room
    # else:
        #print('''Are you sure you've played these games before?''')

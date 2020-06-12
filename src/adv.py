from room import Room
from player import Player
from item import Item

# Declare all the rooms
# reading over and planning still

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 0),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 1),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 2),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 3),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", 4),
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

room['outside'].item.append(Item('sword', 'excalibur'))
room['foyer'].item.append(Item('lamp', 'illuminates the darkness'))
room['overlook'].item.append(Item('map', 'leads the way to treasure'))
room['narrow'].item.append(Item('backpack', 'need a place to store all the items collected'))
room['treasure'].item.append(Item('treasure chest', 'unimaginable riches lie within'))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.



print("Welcome to Neel's House of Terrors!")

player_name = input("Please enter your name: ")
new_player = Player(player_name, room["outside"])

# Write a loop that:
print(new_player)
print('type q to quit')
while True:        
    choice = input("Please choose a direction to move in (n, s, e, w): ")
    try:
        
        if(choice == 'n' or 's' or 'e' or 'w'):
            new_player.movement(choice)        
        elif (choice == 'q'):
            print('Thanks for playing!')
            break
        else:
            print('Please enter a valid option')
    except:
        print('Please enter a valid option')

            

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

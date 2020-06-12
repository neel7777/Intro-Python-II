# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f'Welcome {self.name}, you are currently in room: {self.current_room}'

    def movement(self, direction):
        new_room = getattr(self.current_room, f"{direction}_to")
        if new_room != None:
            self.current_room = new_room
            print(self.current_room)
        else:
            print('Invalid option!')
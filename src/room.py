# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, number):
        self.name = name 
        self.description = description
        
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

        self.item = []
        self.number = number

    def __str__(self):
        return f'{self.name}: {self.description} \nThere is a {self.item[0]} here!'

    #def room_items(self):

    


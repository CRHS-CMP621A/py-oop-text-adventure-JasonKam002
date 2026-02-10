class Room():
    def __init__(self, room_name):
        self.name=room_name
        self.description=None
        self.linked_rooms = {}

    def set_description(self, room_description):
        self.description = room_description
    
    def get_description(self):
        return self.description
    
    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction]=room_to_link

    def get_name(self):
        return self.name
    
    def get_details(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f'The {room.get_name()} is {direction}')

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
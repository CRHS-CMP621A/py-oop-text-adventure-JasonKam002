class Room():
    def __init__(self, room_name):
        self.name=room_name
        self.description=None
        self.linked_rooms = {}
        self.all_items = {}

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
        if self.all_items != False:
            for item_name in self.all_items:
                item_obj = self.all_items[item_name]
                print(f'There is a {item_name}: {item_obj.description}')

        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f'The {room.get_name()} is {direction} to you')

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        elif direction == 'exit':
            return None
        elif direction == 'E' or 'Inv':
            return self
        else:
            print("You can't go that way")
            return self
    
    def add_item(self, item_obj, item_name):
        self.all_items[item_name] = item_obj

    def remove_item(self, item_name):
        del self.all_items[item_name]

    def getitem(self, item_name):
        return self.all_items[item_name]

    
from room import Room

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")
kitchen.describe()

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with")

ball_room = Room("Ballroom")
ball_room.set_description("A vast room with a shiny")


dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ball_room, "west")
kitchen.link_room(dining_hall, "south")
ball_room.link_room(dining_hall, "east")

current_room = kitchen

while True:
    print("\n")
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command)

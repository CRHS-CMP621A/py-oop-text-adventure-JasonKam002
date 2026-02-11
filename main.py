from room import Room
from item import Item

player_inv = []

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with")

ball_room = Room("Ballroom")
ball_room.set_description("A vast room with a shiny")

sword = Item("Sword")
sword.set_description("A scuffed leather sphere with classic pentagon tiles")
soccer = Item("Soccer")
soccer.set_description("A scuffed leather sphere with classic pentagon tiles")
egg = Item("Egg")
egg.set_description("A smooth, speckled oval that feels delicate and strangely warm")


dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ball_room, "west")
kitchen.link_room(dining_hall, "south")
ball_room.link_room(dining_hall, "east")

kitchen.add_item(egg, "Egg")
ball_room.add_item(soccer, "Soccer")
dining_hall.add_item(sword, "Sword")

current_room = kitchen

print('Welcome to the OOP Adventure Game')
command = input('> ')
current_room = current_room.move(command)

while command.lower() != 'exit':
    current_room.get_details()
    command = input('> ')
    current_room = current_room.move(command)
    print('')

    if command == 'E':
        choice = input('Chose the item you want to pick up > ')
        item = current_room.getitem(choice)
        print(f'You have succesfully picked up {item.name}')
        player_inv.append(item)
        current_room.remove_item(choice)

    elif command == 'Inv':
        print('Inventory: ')
        for i in player_inv:
            print(i.name)
            
    else:
        current_room = current_room.move(command)

print('\nThanks for playing')

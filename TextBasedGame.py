# Christine Dickinson

# function to show the player the instructions for the game
def show_instructions():
    print("Climate Change Monster Text Adventure Game")
    print("Collect 6 items to win the game, or your planet becomes uninhabitable")
    print("To move between room, use the move commands: 'South', 'North', 'East', 'West'")
    print("Add to your Inventory: get 'item name'\n")

def main():  # define main function
    show_instructions()
    # A dictionary linking a room to other rooms
    # and linking one item for each room except the Start room (Great Hall) and the room containing the villain
    rooms = {
        'Great Room': {'South': 'Bathroom', 'North': 'Kitchen', 'East': 'Entry Way', 'West': 'Garage'},
        'Bathroom': {'North': 'Great Room', 'East': 'Bedroom Closet', 'item': 'Sunscreen'},
        'Bedroom Closet': {'West': 'Bathroom', 'item': '"Save our home" t-shirt'},
        'Kitchen': {'South': 'Great Room', 'item': 'Klean Kanteen'},
        'Cleaning Pantry': {'East': 'Kitchen', 'item': 'Reusable Rubber Gloves'},
        'Garage': {'East': 'Great Room', 'item': 'Bicycle'},
        'Entry Way': {'West': 'Great Room', 'North': 'Office', 'item': 'Birkenstocks'},
        'Office': {'South': 'Entry Way', 'item': 'Climate Change Monster'}  # monster
    }

    # player starts in the Great Room
    current_room = 'Great Room'
    # player starts with nothing in their inventory
    inventory = []

    # function for moving between rooms
    def next_move(current_room, direction):
        new_room = current_room
        for n in rooms:
            if n == current_room and direction in rooms[n]:
                new_room = rooms[n][direction]

        return new_room

    while True:  # loop for playing the game
        print_status()
        direction = input(
            'Which direction would you like to go? Enter North, South, East, or West. To exit, enter exit. ')  # get the player's next move
        if direction == 'Exit':  # if the player asks to exit
            print('-------------------------------------------')
            print('Thanks for playing my game. I hope you enjoyed it!')
            break
        elif direction == 'North' or direction == 'South' or direction == 'East' or direction == 'West':  # if a valid direction is entered
            new_room = next_move(current_room,
                                 direction)  # run the next_move function to move the player to the next room, if one is there
            if new_room == current_room:  # if there isn't a room in the direction the player chose to go
                print(
                    "\nThere isn't a door on that side. Please choose a different direction.")  # tell them there isn't a door on that side
            else:
                current_room = new_room  # assign the new_room to the current_room
        else:  # if an invalid direction is entered
            print('\nInvalid direction. Please enter North, South, East, or West. To exit, enter exit. ')

        # get player input if they want to pick up item
        if rooms[current_room]['item'] != None:
            print("You see a", rooms[current_room]['item'])
            option = input("get " + rooms[current_room]['item'] + "?(Y/N): ").upper()
            if option != 'Y' and option != 'N':
                print("Invalid input. Try again")
                option = input("Get " + rooms[current_room]['item'] + "?(Y/N): ").upper()
            if option == 'Y':
                inventory.append(rooms[current_room]['item'])
                rooms[current_room]['item'] = None
        else:
            print("Already item collected or nothing in this room")

        # determining if the player won or lost
        if len(inventory) == 6:
            print('Congratulations! You won!')
        else:
            if current_room[item] == 'Climate Change Monster':
                print('Oh no! The Climate Change Monster is here and your planet is no longer inhabitable.')
                print('Planet, and game, lost')

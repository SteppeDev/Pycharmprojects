# Cyber-lair by Oleg Kruter

rooms = {
    'Grand Hall': {
        'South': 'Sewer System',
        'West': 'Weapons Depot',
        'East': 'Cybernetics Lab',
        'North': 'Cyber-Lair',
        'item': None
    },
    'Cyber-Lair': {
        'South': 'Grand Hall',
        'item': 'Cyber-Dragon',
        'defeated': False
    },  # Villain
    'Weapons Depot': {
        'East': 'Grand Hall',
        'South': 'Cyber-interrogation chamber',
        'item': 'Laser arms'
    },
    'Cyber-interrogation chamber': {
        'North': 'Weapons Depot',
        'West': 'Defense tower West',
        'East': 'Sewer System',
        'item': 'Cyber-speed legs'
    },
    'Defense tower West': {
        'East': 'Cyber-interrogation chamber',
        'item': 'Heat Shield'
    },
    'Sewer System': {
        'North': 'Grand Hall',
        'West': 'Cyber-interrogation chamber',
        'East': 'Cyber-Dungeon',
        'South': 'Castle Cyber-Entrance',
        'item': 'X-ray eye implant'
    },
    'Castle Cyber-Entrance': {
        'North': 'Sewer System',
        'item': None
    },
    'Cyber-Dungeon': {
        'North': 'Cybernetics Lab',
        'West': 'Sewer System',
        'East': 'Defense tower East',
        'item': 'Cyborg decoy'
    },
    'Defense tower East': {
        'West': 'Cyber-Dungeon',
        'item': 'cloaking skin implant'
    },
    'Cybernetics Lab': {
        'West': 'Grand Hall',
        'South': 'Cyber-Dungeon',
        'item': 'slow motion neuro-chip'
    }

}

# Step 2: Set the current room to the starting room
current_room = 'Castle Cyber-Entrance'  # Starting in the Great Hall
# Player's inventory to store picked items
inventory = []


# Step 3: Display the description of the current room to the player
def display_current_room():
    print(f"\nYou are in the {current_room}.")
    item = rooms[current_room]['item']
    if item:
        print(f"You see a {item} here.")
    else:
        print("This room is empty.")


def check_boss_defeat():
    required_items = ['laser arms', 'slow motion neuro-chip', 'cyber-speed legs'
                      'X-ray eye implant', 'Cyborg decoy', 'Heat Shield', 'cloaking skin implant']
    if all(item in inventory for item in required_items):
        print("You have gathered all the items!")
        print("You defeat the boss with your combined power!")
        rooms['Cyber-Lair']['defeated'] = True
    else:
        print("You are not strong enough to defeat the boss.")
        return False
    return True


def restart_game():
    global current_room, inventory
    current_room = 'Castle Cyber-Entrance'
    inventory = []
    print("The game has been restarted!")


# Main game loop
while True:
    display_current_room()  # Show the current room description and item

    # Step 4a: Prompt the player to choose a direction, pick up an item, or quit
    choice = input(
        "Choose a direction (North, South, East, West), type 'pick up' to collect the item, or 'quit' to exit: ").capitalize()

    # Step 4b: If the player chooses to quit, end the game
    if choice == 'Quit':
        print("Thank you for playing!")
        break

    # Step 4c: If the player chooses a direction
    if choice in ['North', 'South', 'East', 'West']:
        # Check if the chosen direction is valid from the current room
        if choice in rooms[current_room]:
            # Update the current room to the new room
            current_room = rooms[current_room][choice]
        else:
            print("You can't go that way!")

    # Option to pick up an item
    elif choice == 'Pick up':
        item = rooms[current_room]['item']
        if item:
            inventory.append(item)  # Add item to inventory
            rooms[current_room]['item'] = None  # Remove item from the room
            print(f"You picked up a {item}.")
        else:
            print("There are no items to pick up here.")
    elif choice == 'Fight':
        if current_room == 'Cyber-Lair':
            if not check_boss_defeat():
                print("You were defeated by the Cyber-dragon!")
                restart_choice = input("Would you like to restart the game or quit? (restart/quit): ").lower()
                if restart_choice == 'restart':
                    restart_game()
                elif restart_choice == 'quit':
                    print("Thank you for playing!")
                    break
                else:
                    print("Invalid choice. Please type 'restart' or 'quit'.")
        else:
            print("There's no boss to fight here.")
    else:
        print("Invalid choice. Please choose a valid direction, 'pick up', or 'quit'.")

    # Show current inventory
    if inventory:
        print("Your inventory: " + ', '.join(inventory))
    if current_room == 'Cyber-Lair' and rooms['Cyber-Lair']['defeated']:
        print("You have defeated the dragon!")
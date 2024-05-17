# main.py

def welcome_message():
    print("Welcome to the Digital Escape Room!")
    print("You need to solve puzzles to escape each room.")
    print("Good luck!\n")

def main():
    welcome_message()
    current_room = "room1"
    
    while current_room:
        if current_room == "room1":
            from rooms.room1 import room1
            current_room = room1()
        elif current_room == "room2":
            from rooms.room2 import room2
            current_room = room2()
        # Add more rooms as needed
        
    print("Congratulations! You've escaped the digital escape room!")

if __name__ == "__main__":
    main()

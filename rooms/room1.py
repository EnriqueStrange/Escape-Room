# rooms/room1.py

def room1():
    print("You are in Room 1. There is a locked door and a puzzle on the wall.")
    # Call a puzzle function (to be created in the puzzles folder)
    from puzzles.puzzle1 import solve_puzzle1
    
    solved = solve_puzzle1()
    if solved:
        print("You solved the puzzle! The door to Room 2 is now open.")
        return "room2"
    else:
        print("You failed to solve the puzzle. Try again.")
        return "room1"

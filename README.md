# Digital Escape Room

Welcome to the Digital Escape Room! This project is a Python-based interactive escape room game where players solve puzzles to progress through various rooms and ultimately escape. Each room presents a unique challenge that must be overcome to move to the next.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Interactive Puzzles:** Solve various puzzles to unlock the next room.
- **Text-based Adventure:** Simple text-based interface for ease of use.
- **Modular Design:** Easily add or modify rooms and puzzles.

## Requirements
- Python 3.7 or higher

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/digital-escape-room.git
   cd digital-escape-room
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv escape_room_env
   ```

3. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     escape_room_env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source escape_room_env/bin/activate
     ```

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To start the game, run the `main.py` file:
```bash
python main.py
```
Follow the on-screen instructions to navigate through rooms and solve puzzles.

## Project Structure
```
digital-escape_room/
│
├── main.py
├── rooms/
│   ├── room1.py
│   ├── room2.py
│   └── ...
├── puzzles/
│   ├── puzzle1.py
│   ├── puzzle2.py
│   └── ...
└── assets/
    ├── images/
    └── ...
```

- `main.py`: The main game loop controlling the flow of the game.
- `rooms/`: Contains modules for each room in the escape room.
- `puzzles/`: Contains modules for each puzzle.
- `assets/`: (Optional) Contains additional assets like images or sounds.

### Example of a Room (`rooms/room1.py`)
```python
def room1():
    print("You are in Room 1. There is a locked door and a puzzle on the wall.")
    from puzzles.puzzle1 import solve_puzzle1
    
    solved = solve_puzzle1()
    if solved:
        print("You solved the puzzle! The door to Room 2 is now open.")
        return "room2"
    else:
        print("You failed to solve the puzzle. Try again.")
        return "room1"
```

### Example of a Puzzle (`puzzles/puzzle1.py`)
```python
def solve_puzzle1():
    print("Puzzle 1: What is 2 + 2?")
    answer = input("Enter your answer: ")
    
    if answer == "4":
        return True
    else:
        return False
```

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any enhancements, bug fixes, or new features.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
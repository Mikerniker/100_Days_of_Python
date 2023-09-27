# This is in progress 

board = [["_", "_", "_"] for i in range(3)]
for i in board:
    print(i)

# Dictionary to map position on the board
board_position = {
    "1": (0, 0), "2": (0, 1), "3": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "7": (2, 0), "8": (2, 1), "9": (2, 2)
}
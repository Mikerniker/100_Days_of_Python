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

# Function to update the board and board_position
def update_board(position, player):
    row, col = board_position[position]
    if board[row][col] == "_":
        board[row][col] = player
    else:
        print("That's not available.")


def choose_player():
    player = input("Select Player, type 'X' or 'O': ").upper()
    if player != "X" and player != "O":
        print("Please make sure to type X or O")
        return choose_player()
    else:
        return player
    

def check(list, player):
    return all(i == player for i in list)


def check_winner(player):
    # all_rows = [board[i] for i in range(3)]
    row1 = board[0]
    row2 = board[1]
    row3 = board[2]
    column1 = [board[i][0] for i in range(3)]
    column2 = [board[i][1] for i in range(3)]
    column3 = [board[i][2] for i in range(3)]
    diag_left_right = [board[i][i] for i in range(3)]
    diag_right_left = [board[i][2 - i] for i in range(3)]
    check_board = [row1, row2, row3, column1, column2, column3, diag_left_right, diag_right_left]
    for item in check_board:
        if check(item, player):
            print(f"Player: {player} wins!")
            return True
        

def game_play(player):
    player_move = input(f"Player {player}, Choose your position (Type numbers 1-9): ")
    update_board(player_move, player)
    for i in board:
        print(i)


player = choose_player()
print(f"You selected player {player}")
play_game = True

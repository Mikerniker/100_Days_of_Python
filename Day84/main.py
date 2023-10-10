import random


# Dictionary to map position on the board
board_position = {
    "1": (0, 0), "2": (0, 1), "3": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "7": (2, 0), "8": (2, 1), "9": (2, 2)
}

board = [["_", "_", "_"] for i in range(3)]


def update_board(position, player):
    """ Function to update the board and board_position"""
    row, col = board_position[position]
    if board[row][col] == "_":
        board[row][col] = player
    else:
        if player == "player":
            print("That's not available. Pick again")
            game_play(player)
        else:
            computer_move()


def check(list, player):
    """ Function to check if the items in a list are all true"""
    return all(i == player for i in list)


def check_winner(player):
    """ Function to if there's a winner"""
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
            return True


def game_play(player):
    """Function to get players position and update the board"""
    for i in board:
        print(i)
    player_move = input(f"Player {player}, Choose your position (Type numbers 1-9): ")
    if player_move.isdigit() and 1 <= int(player_move) <= 9:
        update_board(player_move, player)
        if check_winner(player):
            for i in board:
                print(i)
            print(f"Player: {player} wins!")
            return True


def computer_move():
    """Function for the computer to choose a spot on the board"""
    board_choice = str(random.randint(1, 9))
    update_board(board_choice, computer_ai)
    if check_winner(computer_ai):
        for i in board:
            print(i)
        print(f"Computer {computer_ai} wins!")
        return True


def choose_player():
    """Function for the players to choose X or O"""
    player = input("Select Player, type 'X' or 'O': ").upper()
    if player != "X" and player != "O":
        print("Please make sure to type X or O")
        return choose_player()
    else:
        return player


game_type = input("Do you want to play with the computer or with a friend, type 'C' for computer, or 'F' for friend: ").upper()

play_game = True

if game_type == "C":
    player = choose_player()
    turn = player
    print(f"You selected player {player}")
    computer_ai = "O" if player == "X" else "X"

    while play_game:
        if turn == player:
            if game_play(turn):
                play_game = False
            turn = computer_ai
        else:
            if computer_move():
                play_game = False
            turn = player

elif game_type == "F":
    player = choose_player()
    print(f"You selected player {player}")

    while play_game:
        if player == "X":
            if game_play(player):
                play_game = False
            player = "O"
        else:
            if game_play(player):
                play_game = False
            player = "X"
else:
    print("Make sure you type 'F' for friend or 'C' for computer.")

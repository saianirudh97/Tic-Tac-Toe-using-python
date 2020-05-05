#board
board = ["-" , "-" , "-",
        "-" , "-" , "-",
        "-" , "-" , "-"]
game_still_going = True
winner = None
current_player = "X"
#displayboard
def display_board():
        print(board[0]+"|"+board[1]+"|"+board[2])
        print(board[3]+"|"+board[4]+"|"+board[5])
        print(board[6]+"|"+board[7]+"|"+board[8])
game_still_going = True
current_player = "X"

#Playgame
def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()

    if winner == "X" or winner == "O":
        print("The winner is " + winner + ".")
    elif winner == None:
        print("Its a tie.")
#checkwin

    #checkrows


    #check columns

    #check diagonals
#handle turn
def handle_turn(player):
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    if position>9:
        print("Enter a value in between 0 and 9")
    else:    
        board[position] = player
        flip_player()
        display_board()
        print("It is "+current_player+" turn")
def check_if_game_over():
    check_if_win()
    check_if_tie()



#check_if_win
def check_if_win():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return
def check_rows():
    global game_still_going
    row_1 =  board[0] == board[1] == board[2] != "-"
    row_2 =  board[3] == board[4] == board[5] != "-"
    row_3 =  board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return



def check_columns():
    global game_still_going
    column_1 =  board[0] == board[3] == board[6] != "-" 
    column_2 =  board[1] == board[4] == board[7] != "-" 
    column_3 =  board[2] == board[5] == board[8] != "-" 
    

    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return
    

def check_diagonals():
    global game_still_going
    diagonal_1 =  board[0] == board[4] == board[8] != "-"

    diagonal_2 =  board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    return


#checktie
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return
#flipplayer
def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return
play_game()

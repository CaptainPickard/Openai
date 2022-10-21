
# while True:
#     # Get player X input
#     x = input("Player X, enter your move: ")

#     # Get player O input
#     o = input("Player O, enter your move: ")

#     # Check for a winner
#     if check_for_winner(x, o):
#         print("We have a winner!")
#         break

#     # Check for a draw
#     if check_for_draw(x, o):
#         print("It's a draw!")
#         break




# Player 1:

# X

# Player 2:

# O



# {

# (1,1): " ", (1,2): " ", (1,3): " ",
# (2,1): " ", (2,2): " ", (2,3): " ",
# (3,1): " ", (3,2): " ", (3,3): " "
# }





def print_board(board):
    print("The board look like this: \n")

    for i in range(3):
        print(" ", end=" ")
        for j in range(3):
            if board[i*3+j] == 1:
                print("X ", end=" ")
            elif board[i*3+j] == 0:
                print("O ", end=" ")
            elif board[i*3+j] != -1:
                print(board[i*3+j]-1, end=" ")
            else:
                print(" ", end=" ")

        print()

def print_instruction():
    print("Please use the following cell numbers to make your move")
    print_board([2,3,4,5,6,7,8,9,10])

def get_input(turn):
    valid = False
    while not valid:
        try:
            player = input("Where would you like to place " + turn + " (1-9)? ")
            player = int(player)
            if player
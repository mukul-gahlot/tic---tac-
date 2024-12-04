# Initialize the game board
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# Function to display the board
def showboard():
    print(board[1], "|", board[2], "|", board[3])
    print("--+---+--")
    print(board[4], "|", board[5], "|", board[6])
    print("--+---+--")
    print(board[7], "|", board[8], "|", board[9])

# Function to check for a draw
def checkfordraw():
    for value in board.values():
        if value == " ":
            return False
    return True

# Function to check for a winner
def checkforwinner(player):
    if (board[1] == board[2] == board[3] == player or
        board[4] == board[5] == board[6] == player or
        board[7] == board[8] == board[9] == player or
        board[1] == board[4] == board[7] == player or
        board[2] == board[5] == board[8] == player or
        board[3] == board[6] == board[9] == player or
        board[1] == board[5] == board[9] == player or
        board[3] == board[5] == board[7] == player):
        return True
    return False

# Function to insert a player's move
def insert(player, position):
    if board[position] == " ":
        board[position] = player
        showboard()
        if checkforwinner(player):
            print(player, "is the winner!")
            quit()
        if checkfordraw():
            print('Game over, it\'s a draw!')
            quit()
    else:
        print("Space is already taken")
        position = int(input('Enter new position: '))
        insert(player, position)

# Main game loop
showboard()

player1 = "x"
player2 = "o"

while True:
    print(player1, "chance")
    position = int(input('Enter your position: '))
    insert(player1, position)
    
    print(player2, "chance")
    position = int(input('Enter your position: '))
    insert(player2, position)

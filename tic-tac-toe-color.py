import PySimpleGUI as sg

# Function to create the initial game board
def create_board():
    # Create a 3x3 grid of white squares
    board = [[sg.Button('', button_color=('white', 'white'), key=(row, col)) for col in range(3)] for row in range(3)]
    # Use a horizontal layout to place the squares in a single row
    layout = [[sg.Column(board[row]) for row in range(3)]]
    # Return the board and the layout
    return board, layout



# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in range(3):
        if all(cell.ButtonText == player for cell in board[row]):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col].ButtonText == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i].ButtonText == player for i in range(3)):
        return True
    if all(board[i][2-i].ButtonText == player for i in range(3)):
        return True
    # No win
    return False

# Function to check if the board is full
def check_full(board):
    return all(cell.ButtonText != '' for row in board for cell in row)

# Function to update the game board and check for a win or draw
def update_board(board, player, row, col):
    # Update the cell with the player's symbol
    board[row][col].Update(player)
    # Check if the player has won
    if check_win(board, player):
        sg.Popup(f'Player {player} wins!', title='Game Over')
        return True
    # Check if the board is full
    if check_full(board):
        sg.Popup('Draw!', title='Game Over')
        return True
    # Game continues
    return False

# Main function
def main():
    # Create the initial game board
    layout, board = create_board()
    # Create the window
    window = sg.Window('Tic Tac Toe', layout, resizable=True)
    # Initialize variables
    player = 'X'
    game_over = False
    # Main game loop
    while True:
        # Get the next event
        event, values = window.read()
        # Check if the window was closed
        if event == sg.WIN_CLOSED:
            break
        # Check if the "New Game" button was clicked
        if event == 'New Game':
            # Reset the game board
            layout, board = create_board()
            window.Close()
            window = sg.Window('Tic Tac Toe', layout, resizable=True)
            player = 'X'
            game_over = False
            continue
        # Check if a cell was clicked
        if isinstance(event, tuple):
            row, col = event
            # Check if the cell is empty
            if board[row][col].ButtonText == '':
                # Update the game board and check for a win or draw
                game_over = update_board(board, player, row, col)
                # Switch players
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
        # Check if the game is over
        if game_over:
            # Reset the game board and variables
            layout, board = create_board()
            player = 'X'
            game_over = False
    # Close the window
    window.Close()

# Run the main function
if __name__ == '__main__':
    main()

import pygame

# Function to create the initial game board
def create_board():
    # Set the colors for the board
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # red, green, blue
    # Create a 3x3 grid of colored squares
    board = [[pygame.Rect(col*100, row*100, 100, 100) for col in range(3)] for row in range(3)]
    # Fill the squares with their colors
    for row in range(3):
        for col in range(3):
            color = colors[(row+col) % 3]
            pygame.draw.rect(screen, color, board[row][col])
    # Return the board
    return board

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in range(3):
        if all(board[row][col] == player for col in range(3)):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    # No win
    return False

# Function to check if the board is full
def check_full(board):
    return all(cell is not None for row in board for cell in row)

# Function to update the game board and check for a win or draw
def update_board(board, player, row, col):
    # Update the cell with the player's symbol
    board[row][col] = player
    # Check if the player has won
    if check_win(board, player):
        font = pygame.font.Font(None, 36)
        text = font.render(f'Player {player} wins!', True, (0, 0, 0))
        screen.blit(text, (10, 10))
        pygame.display.flip()
        pygame.time.delay(3000)  # Display message for 3 seconds
        return True
    # Check if the board is full
    if check_full(board):
        font = pygame.font.Font(None, 36)
        text = font.render('Draw!', True, (0, 0, 0))
        screen.blit(text, (

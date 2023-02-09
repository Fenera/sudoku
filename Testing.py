import pygame

# Initialize Pygame
pygame.init()

# Set the window size
width, height = 500, 500

# Create the window
window = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("Sudoku")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Define the sudoku board
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Draw the sudoku board
def draw_board(board):
    # Draw the background
    window.fill(white)

    # Draw the grid lines
    for i in range(0, 500, 50):
        pygame.draw.line(window, black, (0, i), (500, i), 1)
        pygame.draw.line(window, black, (i, 0), (i, 500), 1)

    # Draw the numbers on the board
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                font = pygame.font.SysFont("Arial", 30)
                text = font.render(str(board[i][j]), True, black)
                window.blit(text, (j*50+20, i*50+10))

# Get the cell that was clicked
def get_cell(pos):
    x, y = pos
    row = y // 50
    col = x // 50
    return row, col

# Run the game loop
running = True
selected = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            selected = get_cell(event.pos)
        if event.type == pygame.KEYDOWN:
            if selected and event.unicode.isdigit() and 0 < int(event.unicode) < 10:
                row, col = selected
                board[row][col] = int(event.unicode)
                selected = None
    draw_board(board)
    pygame.display.update()

# Quit Pygame
pygame.quit()

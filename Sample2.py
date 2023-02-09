#by Fenera Taye

import pygame
pygame.init()
pygame.font.init()

#Dimension of the window
length = 600
height = 600


#Create a window
window = pygame.display.set_mode((length, height))

#Add a caption/title to the window
pygame.display.set_caption("Sudoku")

#Initialize basic colors for later use
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

#initialize a font
font = pygame.font.SysFont("Arial", 30)

board1 = [
    [5, 6, 0, 0, 8, 0, 4, 3, 7],
    [8, 0, 0, 6, 0, 0, 0, 0, 0],
    [1, 0, 0, 2, 0, 3, 6, 8, 5],
    [0, 4, 0, 0, 2, 0, 5, 7, 3],
    [7, 5, 0, 3, 0, 4, 0, 2, 8],
    [0, 0, 8, 0, 0, 0, 1, 6, 0],
    [0, 0, 3, 9, 0, 0, 0, 5, 0],
    [6, 0, 0, 4, 0, 0, 0, 9, 2],
    [2, 0, 0, 5, 0, 8, 3, 0, 0]
        ]

#Function that displays the grid as an actual board
def draw_board(grid):

    #changes the background color of window
    window.fill(white)

    #Draw the horizontal and vertical lines(respectively)
    #Parameters: line(surface, color, start_pos, end_pos, thickness of line)

    width_of_line = 3
    for i in range(0, 600, 60):

        pygame.draw.line(window, black, (0, i), (540, i), width_of_line) #Horizontal Line
        pygame.draw.line(window, black, (i, 0), (i, 540), width_of_line) #Vertical line

    #Draw the numbers in the cells
    for i in range(9):
        for j in range(9):
            if board1[i][j] != 0:
                #render(text, antialias(T or F), color, background=None) -> Surface AKA creating the text
                number = font.render(str(board1[i][j]), True, black)
                #Places number above on screen
                window.blit(number, (j * 60 + 20, i * 60 + 10)) #blit(text, location)

#A function that looks for the position of the cell clicked by the user's mouse and returns it as (Row, Col)
def get_cell(pos):
    (x, y) = pos

    #returns row(as an integer) //60 because the row can only be 0 - 600 and each cell is 60 by 60
    row = y // 60
    col = x // 60

    return (row, col)


run = True
cell_clicked = None #initializes the cell clicked to empty

while run:

    for event in pygame.event.get(): #gets event/action
        if event.type == pygame.QUIT:#checks if user pressed x to exit
            run = False

        #checks if user pressed their mouse(left key) and gets the position of the cell clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #checks if user pressed left mouse key(1 denotes left key, 2 right..)
            cell_clicked = get_cell(event.pos)

        #Gets the number the user enters when they press a button on their keyboard & checks if it is a valid value
        if event.type == pygame.KEYDOWN:
            if cell_clicked and event.unicode.isdigit() and 0 < int(event.unicode) < 10: #is the value a digit & is it 1 - 9
                row, col = cell_clicked #sets the row and column to the cell that was clicked
                board1[row][col] = int(event.unicode)
                cell_clicked = None #Resets the value of the cell clicked so it can be reused

    draw_board(board1) #calls function made earlier
    pygame.display.update() #constantly updates the screen while the game is running


#Quits if run = False
pygame.quit()

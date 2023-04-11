#by Fenera Taye

#1 from questions import quiz(quiz being the dictionary that stores the questions and their corresponding answers)
#2 use for i in quiz to access individual questions(for-each loop)
#3

import pygame
pygame.init()
pygame.font.init()

#Dimension of the window
length = 700
height = 700


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
modern1 = (231, 230, 230)
modern2 = (93, 142, 193)
modern3 = (14, 52, 91)

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
    window.fill(modern1)

    #Draw the horizontal and vertical lines(respectively)
    #Parameters: line(surface, color, start_pos, end_pos, thickness of line)
    for i in range(100, 600, 50):
        if i % 150 == 100:
            width_of_line = 6
            color_of_lines = modern3
        else:
            width_of_line = 2
            color_of_lines = modern2
        pygame.draw.line(window, color_of_lines, (100, i), (550, i), width_of_line) #Horizontal Line
        pygame.draw.line(window, color_of_lines, (i, 100), (i, 550), width_of_line) #Vertical line

    #Draw the numbers in the cells
    for i in range(9):
        for j in range(9):
            if board1[i][j] != 0:
                #render(text, antialias(T or F), color, background=None) -> Surface AKA creating the text
                number = font.render(str(board1[i][j]), True, black)
                #Places number above on screen
                window.blit(number, (j * 50 + 120, i * 50 + 110)) #blit(text, location)

#A function that looks for the position of the cell clicked by the user's mouse and returns it as (Row, Col)
def get_cell(pos):
    (x, y) = pos

    #returns row(as an integer) //60 because the row can only be 0 - 600 and each cell is 60 by 60
    row = (y - 100) // 50
    col = (x - 100) // 50

    return (row, col)

#A function that highlights the borders of the cell the user clicks
def highlight_cell_clicked(cell_clicked):
    if cell_clicked: #. If selected is false (e.g. None), else true if it has a real value
        row, col = cell_clicked
        #draws a rectangle around cell clicked
        #Parameters(surface, color, (location(x, y) and dimensions(l = 50, h = 50), width of the line)
        pygame.draw.rect(window, red, (col*50+100, row*50+100, 50, 50), 3)


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
                highlight_cell_clicked(cell_clicked)
                row, col = cell_clicked #sets the row and column to the cell that was clicked
                board1[row][col] = int(event.unicode)

                cell_clicked = None #Resets the value of the cell clicked so it can be reused

    draw_board(board1) #calls function made earlier
    pygame.display.update() #constantly updates the screen while the game is running


#Quits if run = False
pygame.quit()

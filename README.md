#Testing(To be continued)

import pygame
pygame.init()

pygame.font.init()
font = pygame.font.SysFont("arialblack", 45)


WIDTH = 1000
backgroundColor = (255, 255, 255)

Window = pygame.display.set_mode((WIDTH, WIDTH)  )  # 2
pygame.display.set_caption("Sudoku"  )  # 3
lineWidth = 3
orig_grid_color = (150, 240, 25)
running = True
buffer = 1

#Default Board #1
grid1 = [
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
original_grid = [[grid1[x][y] for y in range(len(grid1[0]))] for x in range(len(grid1))]


def insert(win, position):
    i, j = position[1], position[0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                #1. User tries to edit original file
                if(original_grid[i-1][j-1] != 0):
                    return
                #2. Edit
                if(event.key == 48): #Checking w/ 0
                    grid1[i-1][j-1] = event.key - 48
                    #Adds a new layer on top of existing number when user edits
                    pygame.draw.rect(win, backgroundColor, (position[0] * 91 + buffer, position[1] * 91 + buffer, 91 - buffer, 91 - buffer))
                    pygame.display.update()
                #3. Adding the digits
                if(0 < event.key - 48 < 10): #Checking for valid input
                        pygame.draw.rect(win, backgroundColor, (
                        position[0] * 91 + buffer, position[1] * 91 + buffer, 91 - buffer, 91 - buffer))
                        value = font.render(str(event.key - 48), True, (0,0,0)) #New Value
                        Window.blit(value, (position[0] * 91 + 15, position[1] * 91))
                        grid1[i-1][j-1] = event.key - 48
                        pygame.display.update()
                return
            return






def main():
    Window.fill(backgroundColor)

    # Determines the width of lines
    for i in range(0, 10):

        if(i % 3 == 0):
            lineWidth = 8
        else:
            lineWidth = 3
        # draws the line || #(surface, color, start_pos, end_pos, width of line)
        pygame.draw.line(Window, (0 ,0 ,0), (91 + 91 * i, 91), (91 + 91 * i, 910), lineWidth)  # VERTICAL LINE
        pygame.draw.line(Window, (0 ,0 ,0), (91, 91 + 91 * i), (910, 91 + 91 * i), lineWidth)  # HORIZONTAL LINE
    pygame.display.update()

    #Fill in the board
    for i in range(0, len(grid1[0])):
        for j in range(0, len(grid1[0])):
            if(0 < grid1[i][j] < 10):
                # render(text, antialias, color, background=None) -> Surface
                value = font.render(str(grid1[i][j]), True, orig_grid_color)
                # blit(surface object, coordinate)
                Window.blit(value, ((j + 1) * 91 + 30, (i + 1) * 91 + 14))
    pygame.display.update()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1  :# Checks if mouse is pressed and if it is a left click
                pos = pygame.mouse.get_pos()
                insert(Window, (pos[0] // 91, pos[1] // 91))


            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()

import pygame
import time

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((1200,950)) #(Width, Height)

pygame.display.set_caption("Sudoku Beta")
font = pygame.font.SysFont("arialblack", 45)

BLUE = pygame.Color((60, 121, 245))

sizer = 75
x = 0 #Initialize x & y
z = 0
lineWidth = 8
val = 500/9
 #Error: it is displaying grid backwards

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


def draw():

    window.fill(BLUE)

    
    

    

    for i in range(9):
        for j in range(9):
            if board1[i][j] != 0:
                pass
                pygame.draw.rect(window, (216, 100, 25), (i * sizer, j * sizer, sizer + 1, sizer + 1) ) # Colors the box that has the numbers Note: 75 represents size of color
                text1 = font.render(str(board1[i][j]), 1, (0, 0, 0))
                window.blit(text1, (i * sizer + 15, j * sizer + 15))
                #Note:rect(surface, color, rect)
    for i in range(10):
        if i % 3 == 0:
            lineWidth = 9
        else:
            lineWidth = 3
        
        pygame.draw.line(window, (0,0,0), (0, i * sizer), (678, i * sizer), lineWidth) #Horizontal lines
        pygame.draw.line(window, (0,0,0), (i * sizer, 0), (i * sizer, 678), (lineWidth)) #Vertical lines
        #Note: line(surface, color, start_pos, end_pos, width=1)
    pygame.display.update()
    

def get_position(pos):
    global x
    x = pos[0] // sizer
    global y
    z = pos[1] // sizer


def highlight_cell():
    for f in range(2):
        pygame.draw.line(window, (168, 255, 220), (x * sizer -3, (f + z) * sizer), (x * sizer + sizer + 3, (z + f) * sizer), 7 )
        pygame.draw.line(window, (168, 255, 220), ( (x + f) * sizer, z * sizer), ((x + f) * sizer, z * sizer + sizer), 7)




def main():

    clock = pygame.time.Clock()

    run = True

    while run:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                get_position(pos)
                
                


        draw()

main()















    
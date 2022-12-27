import pygame
import requests


WIDTH = 1000
background_color = (255,222,173)
color1 = (255, 0, 0)
size_of_lines = 2

#response = requests.get


def main():
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku")
    WIN.fill(background_color)

    for i in range(0, 10):
        if i % 3 == 0:
            color1 = (0, 0, 255)
            size_of_lines = 4
        else:
            color1 = (0, 0, 0)
            size_of_lines = 2
        pygame.draw.line(WIN, (color1), (91 + 91 * i, 91), (91 + 91 * i ,909), size_of_lines) # Color, Starting Coor., Ending coor., Width of line
        pygame.draw.line(WIN, (color1), (91, 91 + 91 * i), (909, 91 + 91 * i), size_of_lines) #Same thing as above(for vertical lines)
        pygame.display.update()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()
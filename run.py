# python code goes here
import pygame
import os
pygame.font.init()
pygame.mixer.init()

# Global variables
WIDTH, HEIGHT = 1050, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aliens Vs Nasa!")

# colours for the window
GRAY = (102, 102, 102)

# frames per second
FPS = 60


# drawing function
def drawing_elements():
    WIN.fill(GRAY)
    pygame.display.update()


# main function
def main():
    """
    Handles the main loop and the logic of the game.
    """
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        drawing_elements()
        
    pygame.quit()

if __name__ == '__main__':
    main()

# python code goes here
import pygame
import os
pygame.font.init()
pygame.mixer.init()

# Global variables
WIDTH, HEIGHT = 1050, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aliens Vs Nasa!")

GRAY = (102, 102, 102)

# main function
def main():
    """
    Handles the main loop and the logic of the game.
    """
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        WIN.fill(GRAY)
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()

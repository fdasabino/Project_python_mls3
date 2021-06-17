# python code goes here
import pygame
import os
pygame.font.init()
pygame.mixer.init()

# Global variables
WIDTH, HEIGHT = 1050, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nasa Vs Aliens!")

# colours for the window
GRAY = (102, 102, 102)

# frames per second
FPS = 60

# images + sizes
SHIPS_WIDTH, SHIPS_HEIGHT = 80, 80

# left spaceship
NASA_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets','nasa.png'))
NASA_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(NASA_SPACESHIP_IMG, (SHIPS_WIDTH, SHIPS_HEIGHT)), 270)

# right spaceship
ALIEN_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets','alien.png'))
ALIEN_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(ALIEN_SPACESHIP_IMG, (SHIPS_WIDTH, SHIPS_HEIGHT)), 90)

# drawing function
def drawing_elements():
    """
    Draws the elements in the screen.
    PS: it's important to draw the elements on the right order.
    """
    WIN.fill(GRAY) # background
    WIN.blit(NASA_SPACESHIP, (300, 300)) # nasa
    WIN.blit(ALIEN_SPACESHIP, (600, 300)) # alien
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

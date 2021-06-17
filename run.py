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
BLUE = (0, 119, 204)

# frames per second
FPS = 60

# velocity
VEL = 8

# images + sizes
SHIPS_WIDTH, SHIPS_HEIGHT = 80, 80

# screen middle division
BORDER = pygame.Rect(WIDTH/2 - 3, 0, 6, HEIGHT)

# left spaceship
NASA_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets','nasa.png'))
NASA_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(NASA_SPACESHIP_IMG, (SHIPS_WIDTH, SHIPS_HEIGHT)), 270)

# right spaceship
ALIEN_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets','alien.png'))
ALIEN_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(ALIEN_SPACESHIP_IMG, (SHIPS_WIDTH, SHIPS_HEIGHT)), 90)

# drawing function
def drawing_elements(alien, nasa):
    """
    Draws the elements in the screen.
    PS: it's important to draw the elements on the right order.
    """
    WIN.fill(GRAY) # background
    pygame.draw.rect(WIN, BLUE, BORDER)
    WIN.blit(NASA_SPACESHIP, (nasa.x, nasa.y)) # nasa
    WIN.blit(ALIEN_SPACESHIP, (alien.x, alien.y)) # alien
    pygame.display.update()

# movement function nasa ship
def movement_function_nasa(keys_pressed, nasa):
        # nasa ship controls
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]: # left
            nasa.x -= VEL  
        if keys_pressed[pygame.K_d]: # right
            nasa.x += VEL  
        if keys_pressed[pygame.K_w]: # up
            nasa.y -= VEL  
        if keys_pressed[pygame.K_s]: # down
            nasa.y += VEL  

# movement function alien ship
def movement_function_alien(keys_pressed, alien):
        # nasa ship controls
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]: # left
            alien.x -= VEL  
        if keys_pressed[pygame.K_RIGHT]: # right
            alien.x += VEL  
        if keys_pressed[pygame.K_UP]: # up
            alien.y -= VEL  
        if keys_pressed[pygame.K_DOWN]: # down
            alien.y += VEL  
            

# main function
def main():
    """
    Handles the main loop and the logic of the game.
    """
    nasa = pygame.Rect(100, 300, SHIPS_WIDTH, SHIPS_HEIGHT)
    alien = pygame.Rect(700, 300, SHIPS_WIDTH, SHIPS_HEIGHT)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        keys_pressed = pygame.key.get_pressed()
        movement_function_nasa(keys_pressed, nasa)
        movement_function_alien(keys_pressed, alien)
        drawing_elements(alien, nasa)
        
    pygame.quit()

if __name__ == '__main__':
    main()

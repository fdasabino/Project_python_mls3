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
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# frames per second
FPS = 60

# velocity
VEL = 8

# bullets
BULLET_VEL = 8
MAX_BULLETS = 5

# images + sizes
SHIPS_WIDTH, SHIPS_HEIGHT = 80, 80

# screen middle division
BORDER = pygame.Rect(WIDTH//2 - 3, 0, 6, HEIGHT)

# hit events 
NASA_HIT = pygame.USEREVENT + 1
ALIEN_HIT = pygame.USEREVENT + 2


# left spaceship
NASA_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets','nasa.png'))
NASA_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(NASA_SPACESHIP_IMG, (SHIPS_WIDTH, SHIPS_HEIGHT)), 270)

# right spaceship
ALIEN_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets','alien.png'))
ALIEN_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(ALIEN_SPACESHIP_IMG, (SHIPS_WIDTH, SHIPS_HEIGHT)), 90)

# drawing function
def drawing_elements(alien, nasa, nasa_bullets, alien_bullets):
    """
    Draws the elements in the screen.
    PS: it's important to draw the elements on the right order.
    """
    WIN.fill(GRAY) # background
    pygame.draw.rect(WIN, BLUE, BORDER)
    WIN.blit(NASA_SPACESHIP, (nasa.x, nasa.y)) # nasa
    WIN.blit(ALIEN_SPACESHIP, (alien.x, alien.y)) # alien
    pygame.display.update()
    
    for bullet in nasa_bullets:
        pygame.draw.rect(WIN, GREEN, bullet)
        
    for bullet in alien_bullets:
        pygame.draw.rect(WIN, RED, bullet)

# movement function nasa ship
def movement_function_nasa(keys_pressed, nasa):
        # nasa ship controls
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and nasa.x - VEL > 0: # left
            nasa.x -= VEL  
        if keys_pressed[pygame.K_d] and nasa.x + VEL + nasa.width < BORDER.x: # right
            nasa.x += VEL  
        if keys_pressed[pygame.K_w] and nasa.y - VEL > 0: # up
            nasa.y -= VEL  
        if keys_pressed[pygame.K_s] and nasa.y + VEL + nasa.height < HEIGHT: # down
            nasa.y += VEL  

# movement function alien ship
def movement_function_alien(keys_pressed, alien):
        # nasa ship controls
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and alien.x - VEL > BORDER.x + BORDER.width: # left
            alien.x -= VEL  
        if keys_pressed[pygame.K_RIGHT] and alien.x + VEL + alien.width < WIDTH: # right
            alien.x += VEL  
        if keys_pressed[pygame.K_UP] and alien.y - VEL > 0: # up
            alien.y -= VEL  
        if keys_pressed[pygame.K_DOWN] and alien.y + VEL + alien.height < HEIGHT - 15: # down
            alien.y += VEL  
# bullets function
def bullets_handle(nasa_bullets, alien_bullets, nasa, alien):
    """
    Handles bullets movement and collision of the fired bullets on the screen 
    """
    for bullet in nasa_bullets:
        bullet.x += BULLET_VEL
        if alien.colliderect(bullet):
            pygame.event.post(pygame.event.Event(ALIEN_HIT))
            nasa_bullets.remove(bullet)
            
    for bullet in alien_bullets:
        bullet.x -= BULLET_VEL
        if nasa.colliderect(bullet):
            pygame.event.post(pygame.event.Event(NASA_HIT))
            nasa_bullets.remove(bullet)

# main function
def main():
    """
    Handles the main loop and the logic of the game.
    """
    nasa = pygame.Rect(100, 300, SHIPS_WIDTH, SHIPS_HEIGHT)
    alien = pygame.Rect(700, 300, SHIPS_WIDTH, SHIPS_HEIGHT)
    
    nasa_bullets = []
    alien_bullets = []
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(nasa_bullets) < MAX_BULLETS: 
                    bullet = pygame.Rect(nasa.x + nasa.width, nasa.y + nasa.height//2 - 2, 10, 5)
                    nasa_bullets.append(bullet)
                    
                if event.key == pygame.K_RCTRL and len(alien_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(alien.x, alien.y + alien.height//2 - 2, 10, 5)
                    alien_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        movement_function_nasa(keys_pressed, nasa)
        movement_function_alien(keys_pressed, alien)
        
        bullets_handle(nasa_bullets, alien_bullets, nasa, alien)
        
        drawing_elements(alien, nasa, nasa_bullets, alien_bullets)
        
    pygame.quit()

if __name__ == '__main__':
    main()

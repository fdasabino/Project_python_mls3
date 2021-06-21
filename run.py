# python code goes here
"""
Imported Libraries and global variables
"""
import os
import pygame
pygame.font.init()
pygame.mixer.init()

# Global variables
WIDTH, HEIGHT = 1300,900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nasa Vs Aliens!")

# colours for the window
WHITE = (255, 255, 255)
GRAY = (102, 102, 102)
BLUE = (0, 119, 204)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# frames per second
FPS = 60

# velocity
VEL = 8

# bullets
BULLET_VEL = 15
MAX_BULLETS = 5

# images + sizes
SHIPS_WIDTH, SHIPS_HEIGHT = 80, 80

# screen middle division
BORDER = pygame.Rect(WIDTH//2 - 3, 0, 6, HEIGHT)

# bullets sound
SOUND_HIT = pygame.mixer.Sound(os.path.join('Assets', 'hit_sound.mp3'))
SOUND_GUN = pygame.mixer.Sound(os.path.join('Assets', 'laser_gun.mp3'))

# texts import
TEXT_FONT = pygame.font.SysFont('arial', 50)

# hit events
NASA_HIT = pygame.USEREVENT + 1
ALIEN_HIT = pygame.USEREVENT + 2

# left spaceship
NASA_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets', 'nasa.png'))
NASA_SPACESHIP = pygame.transform.rotate(pygame.transform.scale
                                         (NASA_SPACESHIP_IMG,(SHIPS_WIDTH, SHIPS_HEIGHT)), 270)

# right spaceship
ALIEN_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets', 'alien.png'))
ALIEN_SPACESHIP = pygame.transform.rotate(pygame.transform.scale
                                          (ALIEN_SPACESHIP_IMG, (SHIPS_WIDTH, SHIPS_HEIGHT)), 90)

# background image
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join
                                                      ('Assets', 'space.jpg')), (WIDTH,HEIGHT))

# drawing function
def drawing_elements(alien, nasa, nasa_bullets, alien_bullets, alien_health, nasa_health):
    """
    Draws the elements in the screen.
    PS: it's important to draw the elements on the right order.
    """
    WIN.blit(BACKGROUND, (0, 0)) # background
    pygame.draw.rect(WIN, BLUE, BORDER)
    nasa_health_text = TEXT_FONT.render("Health: " + str(nasa_health), 1, GREEN) # health status
    alien_health_text = TEXT_FONT.render("Health: " + str(alien_health), 1, RED) # health status
    WIN.blit(nasa_health_text, (10, 10))
    WIN.blit(alien_health_text, (WIDTH - alien_health_text.get_width()- 10, 10))
    WIN.blit(NASA_SPACESHIP, (nasa.x, nasa.y)) # nasa
    WIN.blit(ALIEN_SPACESHIP, (alien.x, alien.y)) # alien

    for bullet in nasa_bullets:
        pygame.draw.rect(WIN, GREEN, bullet)

    for bullet in alien_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    pygame.display.update()

# movement function nasa ship
def movement_function_nasa(keys_pressed, nasa):
    """
    Defines the keys to move the nasa spaceships on the screen
    """
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
    """
    defines the keys to move the alien spaceships on the screen
    """
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
    Handles bullets movement and collision of the fired bullets on the screen.
    """
    for bullet in nasa_bullets:
        bullet.x += BULLET_VEL
        if alien.colliderect(bullet):
            pygame.event.post(pygame.event.Event(ALIEN_HIT))
            nasa_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            nasa_bullets.remove(bullet)

    for bullet in alien_bullets:
        bullet.x -= BULLET_VEL
        if nasa.colliderect(bullet):
            pygame.event.post(pygame.event.Event(NASA_HIT))
            alien_bullets.remove(bullet)
        elif bullet.x < 0:
            alien_bullets.remove(bullet)

# winner function
def winner(text):
    """
    Writes a text with the winner side.
    """
    write_text = TEXT_FONT.render(text, 1, WHITE)
    WIN.blit(write_text, (WIDTH/2 - write_text.get_width()/2, HEIGHT/2 - write_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

# main function
def main():
    """
    Handles the main loop and the logic of the game.
    """
    nasa = pygame.Rect(100, 300, SHIPS_WIDTH, SHIPS_HEIGHT)
    alien = pygame.Rect(700, 300, SHIPS_WIDTH, SHIPS_HEIGHT)

    nasa_bullets = []
    alien_bullets = []

    nasa_health = 10
    alien_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(nasa_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(nasa.x + nasa.width, nasa.y + nasa.height//2 - 2, 10, 5)
                    nasa_bullets.append(bullet)
                    SOUND_GUN.play()

                if event.key == pygame.K_RCTRL and len(alien_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(alien.x, alien.y + alien.height//2 - 2, 10, 5)
                    alien_bullets.append(bullet)
                    SOUND_GUN.play()

            if event.type == NASA_HIT:
                nasa_health -= 1
                SOUND_HIT.play()
            if event.type == ALIEN_HIT:
                alien_health -= 1
                SOUND_HIT.play()

        winner_text = ""
        if nasa_health <= 0:
            winner_text =  "ALIEN SHIP WINS!"
        if alien_health <= 0:
            winner_text = "NASA SHIP WINS!"
        if winner_text != "":
            winner(winner_text)
            break


        keys_pressed = pygame.key.get_pressed()
        movement_function_nasa(keys_pressed, nasa)
        movement_function_alien(keys_pressed, alien)

        bullets_handle(nasa_bullets, alien_bullets, nasa, alien)
        drawing_elements(alien, nasa, nasa_bullets, alien_bullets, alien_health, nasa_health)
    main()
if __name__ == '__main__':
    main()

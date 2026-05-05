import pygame
import math

field = [[0 for _ in range(40)] for _ in range(10)]



width = 10
height = 22
size = 25

def stampa(campo):
    for i in range(10):
        for j in range(20, 40):
            if field[i][j]:
                pygame.draw.rect(screen, "White", (i*size, (j-20)*size+40, size, size))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((width*size, height*size))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 10 * dt
    if keys[pygame.K_s]:
        player_pos.y += 10 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 10 * dt
    if keys[pygame.K_d]:
        player_pos.x += 10 * dt

    field = [[0 for _ in range(40)] for _ in range(10)]
    field[round(player_pos.x % 10)][round(player_pos.y % 20) + 20] = 1
    
    print(round(player_pos.x % 10) )
    print(round(player_pos.y % 20) + 20)

    stampa(field)

    

    # flip() the display to put your work on screen
    pygame.display.flip()


    dt = clock.tick(60) / 1000

pygame.quit()
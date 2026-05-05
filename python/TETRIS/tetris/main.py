import pygame
import math

field = [[0 for _ in range(22)] for _ in range(10)]

def posiziona(pezzo):
    dimensioni = len(pezzo)
    offset_y = 0

    for x in range(dimensioni):
        if sum(pezzo[x]) == 0:
            offset_y += 1
        else:
            break

    for i, riga in enumerate(pezzo):
        for j, cosa, in enumerate(riga):
            if cosa:
                field[4+i][j - offset_y] = 2

def gravity(field):
    # Partiamo dal basso (riga 21) e saliamo verso l'alto (riga 0)
    # range(start, stop, step) -> partiamo da 21, arriviamo a -1, scendendo di 1
    for j in range(21, -1, -1):
        for i in range(10):
            if field[j][i] == 2:
                # 1. Controlliamo se siamo arrivati all'ultima riga
                # 2. O se sotto c'è un pezzo già bloccato (1)
                if j + 1 >= 22 or field[j+1][i] == 1:
                    # Blocca il pezzo: trasforma tutti i '2' in '1'
                    blocca_tutto(field)
                    return # Esci dalla funzione perché il pezzo si è fermato
                else:
                    # Muovi il pezzo in basso
                    field[j+1][i] = 2
                    field[j][i] = 0



PEZZI = {
    'I': [
        [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]],
        [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]],
        [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]],
        [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]
    ],
    'J': [
        [[1, 0, 0], [1, 1, 1], [0, 0, 0]],
        [[0, 1, 1], [0, 1, 0], [0, 1, 0]],
        [[0, 0, 0], [1, 1, 1], [0, 0, 1]],
        [[0, 1, 0], [0, 1, 0], [1, 1, 0]]
    ],
    'L': [
        [[0, 0, 1], [1, 1, 1], [0, 0, 0]],
        [[0, 1, 0], [0, 1, 0], [0, 1, 1]],
        [[0, 0, 0], [1, 1, 1], [1, 0, 0]],
        [[1, 1, 0], [0, 1, 0], [0, 1, 0]]
    ],
    'O': [
        [[1, 1], [1, 1]] # Il quadrato è identico in ogni rotazione
    ],
    'S': [
        [[0, 1, 1], [1, 1, 0], [0, 0, 0]],
        [[0, 1, 0], [0, 1, 1], [0, 0, 1]],
        [[0, 0, 0], [0, 1, 1], [1, 1, 0]],
        [[1, 0, 0], [1, 1, 0], [0, 1, 0]]
    ],
    'T': [
        [[0, 1, 0], [1, 1, 1], [0, 0, 0]],
        [[0, 1, 0], [0, 1, 1], [0, 1, 0]],
        [[0, 0, 0], [1, 1, 1], [0, 1, 0]],
        [[0, 1, 0], [1, 1, 0], [0, 1, 0]]
    ],
    'Z': [
        [[1, 1, 0], [0, 1, 1], [0, 0, 0]],
        [[0, 0, 1], [0, 1, 1], [0, 1, 0]],
        [[0, 0, 0], [1, 1, 0], [0, 1, 1]],
        [[0, 1, 0], [1, 1, 0], [1, 0, 0]]
    ]
}

COLORI = {
    'I': (0, 255, 255),   # Cyan
    'J': (0, 0, 255),     # Blu
    'L': (255, 165, 0),   # Arancione
    'O': (255, 255, 0),   # Giallo
    'S': (0, 255, 0),     # Verde
    'T': (128, 0, 128),   # Viola
    'Z': (255, 0, 0)      # Rosso
}

width = 10
height = 22
size = 25

def stampa(campo):
    for j in range(height): 
        for i in range(width):
           
            if campo[i][j]: 
                
                pygame.draw.rect(screen, "White", (i * size, j * size, size, size))
                
                
                pygame.draw.rect(screen, "Black", (i * size, j * size, size, size), 1)

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
    screen.fill("black")

    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 10 * dt
    if keys[pygame.K_s]:
        player_pos.y += 10 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 10 * dt
    if keys[pygame.K_d]:
        player_pos.x += 10 * dt

    position = (round(player_pos.x % 10), round(player_pos.y % 20) + 20)
    
    posiziona(PEZZI['L'][1])

    stampa(field)

    gravity(field)

    

    # flip() the display to put your work on screen
    pygame.display.flip()


    dt = clock.tick(60) / 1000

pygame.quit()
import pygame
import random
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (105,105,105)

size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)

pygame.display.set_caption("game")

done = False

clock = pygame.time.Clock()

x = 100
y = 400
width = 40
height = 40
vel = 2
health = 500
healthMax = 500
score = 0
playerAlive = True

healthUpX = random.randint(0, 500 - 40)
healthUpY = random.randint(40, 500 - 40)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= vel

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += vel

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= vel

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += vel
    if keys[pygame.K_SPACE] and playerAlive == False:
        playerAlive = True
        score = 0
        health = 500
        healthMax = 500
        x = 100
        y = 400
        healthUpX = random.randint(0, 500 - 40)
        healthUpY = random.randint(40, 500 - 40)
        vel = 2
        
    screen.fill(GREY)

    health -= 1

    if score >= 20:
        healthMax = 250
    if score >= 40:
        healthMax = 125
        vel = 4

    font = pygame.font.Font('freesansbold.ttf', 64)
    text = font.render(str(score), True, (192,192,192))
    screen.blit(text, (250 - 16, 250))

    if playerAlive == True:
        player = pygame.draw.rect(screen, GREEN, [x - width, y - height, width, height])
        healthUp = pygame.draw.rect(screen, WHITE, [healthUpX, healthUpY, 40, 40])
        wall = pygame.draw.rect(screen, WHITE, [0, 0, 500, 40])
        healthBar = pygame.draw.rect(screen, RED, [0, 0, health, 40])

    if health <= 0:
        playerAlive = False

    if player.colliderect(healthUp):
        health = healthMax
        healthUpX = random.randint(0, 500 - 40)
        healthUpY = random.randint(40, 500 - 40)
        score += 1

    if playerAlive == False:
        font2 = pygame.font.Font('freesansbold.ttf', 32)
        text2 = font2.render("You Died", True, (255,255,255))
        text3 = font2.render("Space to reset", True, (255,255,255))
        screen.blit(text2, (250 - 64, 250 - 32))
        screen.blit(text3, (250 - 115, 250 + 64))

    pygame.display.flip()
    clock.tick(60)

pygame.quit
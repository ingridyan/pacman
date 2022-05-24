import pygame
import random
import math

# initialize pygame
from Cast import Cast

pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('notebookbackground.png')
DEFAULT_IMAGE_SIZE = (800, 600)
background = pygame.transform.scale(background, DEFAULT_IMAGE_SIZE)

# title and icon (check flat icon, make sure icon is 32, 32 png)
pygame.display.set_caption("Bae Watch")
icon = pygame.image.load('camera.png')
pygame.display.set_icon(icon)

# player landry
landry = pygame.image.load('landry walking png.png')
DEFAULT_IMAGE_SIZE = (70, 130)
landry = pygame.transform.scale(landry, DEFAULT_IMAGE_SIZE)
leftlandry = pygame.transform.flip(landry, True, False)
landryX = 370
landryY = 300
landryX_change = 0
landryY_change = 0
landryFacingRight = True

score = 0


# score and title
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# title pictures
lan_man_title = pygame.image.load('attackoflanman.png')
DEFAULT_IMAGE_SIZE = (500, 500)
lan_man_title = (pygame.transform.scale(lan_man_title, DEFAULT_IMAGE_SIZE))

def show_titlepage(x, y):
    shown_title = font.render("Ingrid Yan", True, (0, 0, 0))
    screen.blit(shown_title, (x, y))

def show_score(x, y):
    # typecasting
    shown_score = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(shown_score, (x, y))

def landryF(x, y):
    # blit means to draw
    if landryFacingRight == True:
        screen.blit(landry, (x, y))
    else:
        screen.blit(leftlandry, (x, y))

def playerF(x, y, i):
    # blit means to draw
    if playerFacingRight[i] == True:
        screen.blit(player[i], (x, y))
    else:
        screen.blit(leftplayer[i], (x, y))

def isCollision(playerX, playerY, bulletX, bulletY):
    distance = math.sqrt((math.pow(playerX - bulletX, 2)) + (math.pow(playerY - bulletY, 2)))
    if distance < 70:
        return True
    else:
        return False


# load button images
start_img = pygame.image.load('start.png').convert_alpha()
cast_img = pygame.image.load('cast.png').convert_alpha()
playagain_img = pygame.image.load('playagain.png').convert_alpha()

# button class


# create  button instances
Button start_button = new Button(100, 430, start_img, 0.6)
playagain = Button(100, 430, playagain_img, 0.6)
cast_button = Button(550, 430, cast_img, 0.6)
start_button_for_cast = Button(300, 450, cast_img, 0.6)
playagain_for_end = Button(550, 200, playagain_img, 0.6)
# 1st title page
castPage = False
running = False
titlePageRun = True
endPage = False
while titlePageRun:
    screen.blit(background, (0, 0))
    show_titlepage(textX, textY)
    screen.blit(lan_man_title, (150, 50))
    if start_button.draw() == True:
        print("start clicked")
        running = True
        titlePageRun = False
    if cast_button.draw() == True:
        print("cast clicked")
        castPage = True
        titlePageRun = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            titlePageRun = False
    pygame.display.update()

# cast photos
castfont = pygame.font.Font('freesansbold.ttf', 15)
Cast.BioCastPictures()
Cast.liliaBioCast()
Cast.ashlynBioCast()
Cast.alexisBioCast()
Cast.landryBioCast()
Cast.ingridBioCast()

# meet the cast page

while castPage:
    screen.fill((202, 228, 241))
    screen.blit(Cast.alexisCast, (200, 75))
    screen.blit(Cast.landrycast, (50, 75))
    screen.blit(Cast.ashlyncast, (500, 75))
    screen.blit(Cast.liliacast, (350, 75))
    screen.blit(Cast.ingridcast, (650, 75))

    DEFAULT_IMAGE_SIZE = (70, 140)
    landryStand = pygame.image.load('landrystanding png.png')
    landryStand = (pygame.transform.scale(landryStand, DEFAULT_IMAGE_SIZE))
    alexisStand = (pygame.transform.scale(alexisStand, DEFAULT_IMAGE_SIZE))
    DEFAULT_IMAGE_SIZE = (75, 145)
    ingyStand = (pygame.transform.scale(ingyStand, DEFAULT_IMAGE_SIZE))
    screen.blit(landryStand, (50, 400))
    screen.blit(ashlynStand, (558, 450))
    screen.blit(alexisStand, (200, 450))
    screen.blit(liliaStand, (370, 300))
    screen.blit(ingyStand, (700, 450))

    meetthecast = font.render("Meet the Cast", True, (0, 0, 0))
    screen.blit(meetthecast, (50, 0))

    # bios



    if start_button_for_cast.draw() == True:
        print("start clicked")
        running = True
        castPage = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            castPage = False
    pygame.display.update()

# game loop, make sure window doesn't close down
while running:
    screen.fill((133, 186, 204))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether its right or left
        if score == 2:
            running = False
            endPage = True
        if event.type == pygame.KEYDOWN:
            # moving left and right
            if event.key == pygame.K_LEFT:
                if landryFacingRight == True:
                    landryFacingRight = False
                landryX_change = -0.4
            if event.key == pygame.K_RIGHT:
                if landryFacingRight == False:
                    # landry = pygame.transform.flip(landry, True, False)
                    landryFacingRight = True
                landryX_change = 0.4

            # moving up and down
            if event.key == pygame.K_UP:
                landryY_change = -0.4
            if event.key == pygame.K_DOWN:
                landryY_change = 0.4
            # space bar is pressed
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = landryX
                    fire_bullet(bulletX, bulletY)
        # released key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                landryX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                landryY_change = 0

    castfont = pygame.font.Font('freesansbold.ttf', 35)

    while endPage:
        screen.blit(background, (0, 0))
        DEFAULT_IMAGE_SIZE = (450, 450)
        lan_man_title = (pygame.transform.scale(lan_man_title, DEFAULT_IMAGE_SIZE))
        screen.blit(lan_man_title, (50, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endPage = False
        ingridbio = castfont.render("Thanks for playing!", True, (0, 0, 0))
        screen.blit(ingridbio, (100,50))
        if playagain_for_end.draw() == True:
            print("start clicked")
            score = 0
            running = True
            endPage = False
        pygame.display.update()

    # landry movement
    landryX += landryX_change
    if landryX <= 0:
        landryX = 0
    elif landryX >= 730:
        landryX = 730
    landryY += landryY_change
    if landryY <= 350:
        landryY = 350
    elif landryY >= 470:
        landryY = 470

    # player movement
    for i in range(num_of_players):
        playerX[i] += playerX_change[i]
        if playerX[i] <= 0:
            playerX_change[i] = 0.2
            playerFacingRight[i] = True
            playerY[i] += playerY_change[i]
        elif playerX[i] >= 730:
            playerX_change[i] = -0.2
            playerFacingRight[i] = False
            playerY[i] += playerY_change[i]

        # collision
        collision = isCollision(playerX[i], playerY[i], bulletX, bulletY)
        if collision:
            bulletY = 300
            bullet_state = "ready"
            score += 1
            playerX[i] = random.randint(0, 730)
            playerY[i] = random.randint(25, 150)

        playerF(playerX[i], playerY[i], i)



    landryF(landryX, landryY)
    show_score(textX, textY)
    pygame.display.update()

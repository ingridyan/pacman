import pygame
import random
import math

# initialize pygame
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


# player
player = []
playerX = []
playerY = []
playerX_change = []
playerY_change = []
playerFacingRight = []
leftplayer = []
num_of_players = 4

DEFAULT_IMAGE_SIZE_LILIA = (80, 140)
DEFAULT_IMAGE_SIZE_ALEX = (90, 153)
DEFAULT_IMAGE_SIZE_FOR_INGY = (65, 125)
DEFAULT_IMAGE_SIZE_FOR_ASH = (70, 130)

ashlynIMG = pygame.image.load('ashlyn walking png.png')
alexisIMG = pygame.image.load('alexis walking png.png')
liliaIMG = pygame.image.load('lilia png.png')
ingyIMG = pygame.image.load('ingrid walking png.png')

ashlynStand = pygame.image.load('ashlynstanding png.png')
ashlynStand = (pygame.transform.scale(ashlynStand, DEFAULT_IMAGE_SIZE_FOR_ASH))
alexisStand = pygame.image.load('alexisstanding png.png')
alexisStand = (pygame.transform.scale(alexisStand, DEFAULT_IMAGE_SIZE_ALEX))
liliaStand = pygame.image.load('liliastanding png.png')
liliaStand = (pygame.transform.scale(liliaStand, DEFAULT_IMAGE_SIZE))
ingyStand = pygame.image.load('ingridstanding png.png')
ingyStand = (pygame.transform.scale(ingyStand, DEFAULT_IMAGE_SIZE_FOR_INGY))

ashlynIMG = (pygame.transform.scale(ashlynIMG, DEFAULT_IMAGE_SIZE_FOR_ASH))
leftashlynIMG = pygame.transform.flip(ashlynIMG, True, False)
alexisIMG = (pygame.transform.scale(alexisIMG, DEFAULT_IMAGE_SIZE_ALEX))
leftalexisIMG = pygame.transform.flip(alexisIMG, True, False)
liliaIMG = (pygame.transform.scale(liliaIMG, DEFAULT_IMAGE_SIZE_LILIA))
leftliliaIMG = pygame.transform.flip(liliaIMG, True, False)
ingyIMG = (pygame.transform.scale(ingyIMG, DEFAULT_IMAGE_SIZE_FOR_INGY))
leftingyIMG = pygame.transform.flip(ingyIMG, True, False)
score = 0
# 1 is ashlyn
# 2 is alexis
# 3 is ingy
# 4 is lilia

personCounter = 1
for i in range(num_of_players):
    if personCounter == 1:
        player.append(ashlynIMG)
        leftplayer.append(leftashlynIMG)
    elif personCounter == 2:
        player.append(alexisIMG)
        leftplayer.append(leftalexisIMG)
    elif personCounter == 3:
        player.append(ingyIMG)
        leftplayer.append(leftingyIMG)
    else:
        player.append(liliaIMG)
        leftplayer.append(leftliliaIMG)
    playerX.append(random.randint(0, 730))
    playerY.append(random.randint(25, 150))
    playerX_change.append(0.2)
    playerY_change.append(30)
    playerFacingRight.append(True)
    personCounter = (personCounter + 1)

# finger bullet
bullet = pygame.image.load('fingers.png')
DEFAULT_IMAGE_SIZE = (40, 40)
bullet = pygame.transform.scale(bullet, DEFAULT_IMAGE_SIZE)
# ready means you can't see bullet on the screen
# fire means bullet is currently moving
bulletX = 0
bulletY = 300
bulletX_change = 0
bulletY_change = 0.5
bullet_state = "ready"

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


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    if landryFacingRight == True:
        screen.blit(bullet, (x + 50, y))
    if landryFacingRight == False:
        screen.blit(bullet, (x - 50, y))


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
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        # draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


# create  button instances
start_button = Button(100, 430, start_img, 0.6)
playagain = Button(100, 430, playagain_img, 0.6)
cast_button = Button(550, 430, cast_img, 0.6)
start_button_for_cast = Button(300, 450, cast_img, 0.6)
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
alexiscast = pygame.image.load('alexiscast.jpg')
DEFAULT_IMAGE_SIZE = (130, 170)
alexiscast = (pygame.transform.scale(alexiscast, DEFAULT_IMAGE_SIZE))

ashlyncast = pygame.image.load('ashlyncast.jpg')
DEFAULT_IMAGE_SIZE = (130, 170)
ashlyncast = (pygame.transform.scale(ashlyncast, DEFAULT_IMAGE_SIZE))

liliacast = pygame.image.load('liliacast.jpg')
DEFAULT_IMAGE_SIZE = (130, 170)
liliacast = (pygame.transform.scale(liliacast, DEFAULT_IMAGE_SIZE))

landrycast = pygame.image.load('landrycast.jpg')
DEFAULT_IMAGE_SIZE = (130, 170)
landrycast = (pygame.transform.scale(landrycast, DEFAULT_IMAGE_SIZE))

ingridcast = pygame.image.load('ingridcast.jpg')
DEFAULT_IMAGE_SIZE = (130, 170)
ingridcast = (pygame.transform.scale(ingridcast, DEFAULT_IMAGE_SIZE))

castfont = pygame.font.Font('freesansbold.ttf', 15)
# meet the cast page


while castPage:
    screen.fill((202, 228, 241))
    screen.blit(alexiscast, (200, 75))
    screen.blit(landrycast, (50, 75))
    screen.blit(ashlyncast, (500, 75))
    screen.blit(liliacast, (350, 75))
    screen.blit(ingridcast, (650, 75))

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

    liliabio = castfont.render("Lilia:", True, (0, 0, 0))
    screen.blit(liliabio, (380, 250))
    liliabio = castfont.render("ginger.", True, (0, 0, 0))
    screen.blit(liliabio, (380, 275))

    ashlynbio = castfont.render("Ashlyn:", True, (0, 0, 0))
    screen.blit(ashlynbio, (490, 250))
    ashlynbio = castfont.render("incredibly amazing,", True, (0, 0, 0))
    screen.blit(ashlynbio, (490, 275))
    ashlynbio = castfont.render("kind human, who", True, (0, 0, 0))
    screen.blit(ashlynbio, (490, 300))
    ashlynbio = castfont.render("is the biggest,", True, (0, 0, 0))
    screen.blit(ashlynbio, (490, 325))
    ashlynbio = castfont.render("most bestest", True, (0, 0, 0))
    screen.blit(ashlynbio, (490, 350))
    ashlynbio = castfont.render("person ever!", True, (0, 0, 0))
    screen.blit(ashlynbio, (490, 375))
    ashlynbio = castfont.render("That's my bio.", True, (0, 0, 0))
    screen.blit(ashlynbio, (490, 400))
    ashlynbio = castfont.render("Everyone adores,", True, (0, 0, 0))
    screen.blit(ashlynbio, (490, 425))
    ashlynbio = castfont.render("her *of course*", True, (0, 0, 0))
    screen.blit(ashlynbio, (490, 450))
    ashlynbio = castfont.render("Add that.", True, (0, 0, 0))
    screen.blit(ashlynbio, (490, 475))

    alexisbio = castfont.render("alexis:", True, (0, 0, 0))
    screen.blit(alexisbio, (195, 250))
    alexisbio = castfont.render("the swaggiest,", True, (0, 0, 0))
    screen.blit(alexisbio, (195, 275))
    alexisbio = castfont.render("most amazing person", True, (0, 0, 0))
    screen.blit(alexisbio, (195, 300))
    alexisbio = castfont.render("you'll ever meet.", True, (0, 0, 0))
    screen.blit(alexisbio, (195, 325))
    alexisbio = castfont.render("has never broken a ", True, (0, 0, 0))
    screen.blit(alexisbio, (195, 350))
    alexisbio = castfont.render("bone, or recieved a ", True, (0, 0, 0))
    screen.blit(alexisbio, (195, 375))
    alexisbio = castfont.render("B in a class.", True, (0, 0, 0))
    screen.blit(alexisbio, (195, 400))
    alexisbio = castfont.render("However, was once", True, (0, 0, 0))
    screen.blit(alexisbio, (195, 425))
    alexisbio = castfont.render(" sneezed on.", True, (0, 0, 0))
    screen.blit(alexisbio, (195, 450))

    landrybio = castfont.render("Landry:", True, (0, 0, 0))
    screen.blit(landrybio, (35, 250))
    landrybio = castfont.render("the main character", True, (0, 0, 0))
    screen.blit(landrybio, (35, 275))
    landrybio = castfont.render("(only in her eyes)", True, (0, 0, 0))
    screen.blit(landrybio, (35, 300))
    landrybio = castfont.render("and super cool", True, (0, 0, 0))
    screen.blit(landrybio, (35, 325))
    landrybio = castfont.render("and swag and", True, (0, 0, 0))
    screen.blit(landrybio, (35, 350))
    landrybio = castfont.render("and will be famous", True, (0, 0, 0))
    screen.blit(landrybio, (35, 375))

    ingridbio = castfont.render("Ingrid:", True, (0, 0, 0))
    screen.blit(ingridbio, (640, 250))
    ingridbio = castfont.render("plays soccer,", True, (0, 0, 0))
    screen.blit(ingridbio, (640, 275))
    ingridbio = castfont.render("refs 24/7,", True, (0, 0, 0))
    screen.blit(ingridbio, (640, 300))
    ingridbio = castfont.render("hates IHOP,", True, (0, 0, 0))
    screen.blit(ingridbio, (640, 325))
    ingridbio = castfont.render("big fan of acai bowls", True, (0, 0, 0))
    screen.blit(ingridbio, (640, 350))
    ingridbio = castfont.render("killed a bunny whilst", True, (0, 0, 0))
    screen.blit(ingridbio, (640, 375))
    ingridbio = castfont.render("driving the yan van", True, (0, 0, 0))
    screen.blit(ingridbio, (640, 400))

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
        screen.blit(lan_man_title, (170, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endPage = False
        ingridbio = castfont.render("Thanks for playing!", True, (0, 0, 0))
        screen.blit(ingridbio, (100,50))
        if playagain.draw() == True:
            print("start clicked")
            score = 0
            running = True
            endPage = False
        if cast_button.draw() == True:
            print("cast clicked")
            castPage = True
            running = False
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
    # bullet movement

    if bulletY <= 0:
        bulletY = landryY
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    landryF(landryX, landryY)
    show_score(textX, textY)
    pygame.display.update()

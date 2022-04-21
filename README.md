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

# player ashlyn
ashlyn = []
ashlynX = []
ashlynY = []
ashlynX_change = []
ashlynY_change = []
ashlynFacingRight = []
leftashlyn = []
num_of_ashlyns = 6
ashlynIMG = pygame.image.load('ashlyn walking png.png')
DEFAULT_IMAGE_SIZE = (70, 130)
ashlynIMG = (pygame.transform.scale(ashlynIMG, DEFAULT_IMAGE_SIZE))
leftashlynIMG = pygame.transform.flip(ashlynIMG, True, False)

for i in range(num_of_ashlyns) :
    ashlyn.append(ashlynIMG)
    leftashlyn.append(leftashlynIMG)
    ashlynX.append(random.randint(0, 730))
    ashlynY.append(random.randint(25, 150))
    ashlynX_change.append(0.2)
    ashlynY_change.append(30)
    ashlynFacingRight.append(True)


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
score = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

def show_titlepage(x,y):
    shown_title = font.render("Ingrid's Pacman", True, (0, 0, 0))
    screen.blit(shown_title, (x,y))
def show_score(x,y):
    #typecasting
    shown_score = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(shown_score, (x,y))
def landryF(x, y):
    # blit means to draw
    if landryFacingRight == True:
        screen.blit(landry, (x, y))
    else:
        screen.blit(leftlandry, (x, y))

def ashlynF(x, y, i):
    # blit means to draw
    if ashlynFacingRight[i] == True:
        screen.blit(ashlyn[i], (x, y))
    else:
        screen.blit(leftashlyn[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    if landryFacingRight == True:
        screen.blit(bullet, (x + 50, y))
    if landryFacingRight == False:
        screen.blit(bullet, (x - 50, y))

def isCollision(ashlynX, ashlynY, bulletX, bulletY):
    distance = math.sqrt((math.pow(ashlynX - bulletX, 2)) + (math.pow(ashlynY - bulletY, 2)))
    if distance < 70:
        return True
    else:
        return False

#load button images
start_img  = pygame.image.load('start.png').convert_alpha()

#button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        #check mouseover clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        #draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
#create  button instances
start_button = Button(300, 300, start_img, 0.7)

#1st title page.
titlePageRun = True
while titlePageRun:
    screen.fill((202, 228, 241))
    #screen.blit(background, (0,0))
    show_titlepage(textX, textY)

    if start_button.draw() == True:
        print("start clicked")
        running = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            titlePageRun = False
    pygame.display.update()


# game loop, make sure window doesn't close down
running = True
while running:
    screen.fill((133, 186, 204))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            # moving left and right
            if event.key == pygame.K_LEFT:
                if landryFacingRight == True:
                    landryFacingRight = False
                landryX_change = -0.3
            if event.key == pygame.K_RIGHT:
                if landryFacingRight == False:
                    # landry = pygame.transform.flip(landry, True, False)
                    landryFacingRight = True
                landryX_change = 0.3

            # moving up and down
            if event.key == pygame.K_UP:
                landryY_change = -0.3
            if event.key == pygame.K_DOWN:
                landryY_change = 0.3
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

    # landry movement
    landryX += landryX_change
    if landryX <= 0:
        landryX = 0
    elif landryX >= 730:
        landryX = 730
    landryY += landryY_change

    # ashlyn movement
    for i in range(num_of_ashlyns):
        ashlynX[i] += ashlynX_change[i]
        if ashlynX[i] <= 0:
            ashlynX_change[i] = 0.2
            ashlynFacingRight[i] = True
            ashlynY[i] += ashlynY_change[i]
        elif ashlynX[i] >= 730:
            ashlynX_change[i] = -0.2
            ashlynFacingRight[i] = False
            ashlynY[i] += ashlynY_change[i]

        # collision
        collision = isCollision(ashlynX[i], ashlynY[i], bulletX, bulletY)
        if collision:
            bulletY = 300
            bullet_state = "ready"
            score += 1
            ashlynX[i] = random.randint(0, 730)
            ashlynY[i] = random.randint(25, 150)

        ashlynF(ashlynX[i], ashlynY[i], i)
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

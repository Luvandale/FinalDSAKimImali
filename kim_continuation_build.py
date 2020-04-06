import pygame
import random
import math
# a class that helps us handle any kind of music
from pygame import mixer

#  Initialise pygame
pygame.init()

# Creating the Game window
gameWindow = pygame.display.set_mode((800, 600))

# game background
game_background = pygame.image.load('mybackground.png')

# background music
mixer.music.load('background.wav')
mixer.music.play(-1)

# Adding a Game Title
pygame.display.set_caption("Alien Shooter Game")
# Icon for the game
gameIcon = pygame.image.load('enemy.png')
pygame.display.set_icon(gameIcon)

# Defining Player Image and Starting Position of the player
playerIcon = pygame.image.load('space-invaders.png')
playerPosX = 360
playerPosY = 480
# Responsible for the change in direction when user presses left of right key
playerPosx_change = 0

# Enemy
# create a list to store enemies
enemyIcon = []
enemyPosX = []
enemyPosY = []
enemyPosx_change = []
enemyPosy_change = []
number_of_enemies = 7
# Defining Enemy Image and Starting Position of the Enemy
for i in range(number_of_enemies):
    enemyIcon.append(pygame.image.load('enemy.png'))
    # Randomising our enemy start position to the set range
    enemyPosX.append(random.randint(0, 735))
    enemyPosY.append(random.randint(50, 150))
    # Responsible for the change in direction of the enemy
    enemyPosx_change.append(4)
    # this enables the enemy to move downwards by 40 pixels immediately it hits the window
    enemyPosy_change.append(40)

# Bullet
# Defining Enemy Image and Starting Position of the Enemy
bulletIcon = pygame.image.load('bullet.png')
# Randomising our enemy start position to the set range
bulletPosX = 0
# our player is always at 480 and since the bullet is 32 pixels it makes it shorter
bulletPosY = 480
# Responsible for the change in direction of the enemy
bulletPosx_change = 0
# this enables the enemy to move downwards by 40 pixels immediately it hits the window
bulletPosy_change = 10
# set - unable to see the bullet on the screen
# fire - bullet currently moving

bullet_state = 'set'

# variable to show the score value
score = 0
# fontname and the font size
score_font = pygame.font.Font('freesansbold.ttf', 32)
# x and y variable of where we want the score to occur on the screen
scoreX = 10
scoreY = 10
# game over text
gameover_font = pygame.font.Font('freesansbold.ttf', 64)


# function that shows the score on the screen
def display_score(x, y):
    score_value = score_font.render('Score:' + str(score), True, (255, 255, 255))
    gameWindow.blit(score_value, (x, y))


# function that ends the game
def game_over_display():
    gameover_text = gameover_font.render('FUCK YOU LOSER ', True, (255, 255, 255))
    gameWindow.blit(gameover_text, (200, 250))


# Player Character Function
# Arguments x_axis and y_axis to take user input for moving the player accordingly
def player_character(x_axis, y_axis):
    # the blit() method is used to draw the player's Image icon at the defined positions for x and y
    gameWindow.blit(playerIcon, (x_axis, y_axis))


# Enemy Character Function
def enemy_character(x_axis, y_axis, i):
    # the blit() method is used to draw the player's Image icon at the defined positions for x and y
    gameWindow.blit(enemyIcon[i], (x_axis, y_axis))


# fire bullet Function
def fire_bullet(x, y):
    # global variable so that it can be accessed in the function
    global bullet_state
    bullet_state = 'fire'
    # ensures bullet appears at the center of the spaceship
    gameWindow.blit(bulletIcon, (x + 16, y + 10))


#     define whether a collison with the enemy has occurred
def coll_detect(enemyPosX, enemyPosY, bulletPosX, bulletPosY):
    game_distance = math.sqrt((math.pow(enemyPosX - bulletPosX, 2)) + (math.pow(enemyPosY - bulletPosY, 2)))
    if game_distance < 27:
        return True
    else:
        return False


# Game Loop
# Makes sure the game window runs until the Quit button is pressed
gameRunning = True
while gameRunning is True:
    # Changing the game screen's background using RGB codes
    gameWindow.fill((0, 0, 255))
    # background image(prevents the image fro disapperaring after a second)
    gameWindow.blit(game_background, (0, 0))
    # This for loop checks for the event that the quit button is pressed by the user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

        # This Section Handles player movement input along the a axis.
        # If key is pressed check whether it is left or right KEYDOWN - Pressing a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerPosx_change = -5
            if event.key == pygame.K_RIGHT:
                playerPosx_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is 'set':
                    bullet_music = mixer.Sound('laser.wav')
                    bullet_music.play()
                    # gets the x coordinate of the spaceship
                    bulletPosX = playerPosX
                    fire_bullet(bulletPosX, bulletPosY)
        # Check if pressed key has been released KEYUP- Releasing the pressed key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerPosx_change = 0

    # This line updates the player's x-axis position according to the above keyboard press conditions
    playerPosX += playerPosx_change

    # This part is meant to create boundaries around the screen such that the player does not leave the game window
    if playerPosX <= 0:
        playerPosX = 0
    # using 736 because of the size of the object this time 64 pixels so that it can remain within the window
    elif playerPosX >= 736:
        playerPosX = 736

        # Enemy movement
        # This line updates the enemy's x-axis position according to the above keyboard press conditions
    for i in range(number_of_enemies):
        # this code is used in ending the game
        if enemyPosY[i] > 440:
            for j in range(number_of_enemies):
                # ensures the enemies go below the screen
                enemyPosY[j] = 2000
            game_over_display()
            break
        enemyPosX[i] += enemyPosx_change[i]

        # This part is meant to create boundaries around the screen such that the enemy does not leave the game window
        if enemyPosX[i] <= 0:
            enemyPosx_change[i] = 4
            enemyPosY[i] += enemyPosy_change[i]
        # using 736 because of the size of the enemy this time 64 pixels so that it can remain within the window(subtract 64 from 800)
        elif enemyPosX[i] >= 736:
            enemyPosx_change[i] = -4
            enemyPosY[i] += enemyPosy_change[i]
            #     this code handles enemy collision
        character_collision = coll_detect(enemyPosX[i], enemyPosY[i], bulletPosX, bulletPosY)
        if character_collision:
            explosion_music = mixer.Sound('explosion.wav')
            explosion_music.play()
            bulletPosY = 480
            bullet_state = 'set'
            score += 1
            # print(score)
            enemyPosX[i] = random.randint(0, 800)
            enemyPosY[i] = random.randint(50, 150)

        enemy_character(enemyPosX[i], enemyPosY[i], i)
    #     Bullet movement
    if bulletPosY <= 0:
        bulletPosY = 480
        bullet_state = 'set'
    if bullet_state is 'fire':
        fire_bullet(bulletPosX, bulletPosY)
        bulletPosY -= bulletPosy_change

    # Calling our Player to be displayed
    player_character(playerPosX, playerPosY)
    # Calling our Enemy to be displayed
    display_score(scoreX, scoreY)
    # constantly updating our game window
    pygame.display.update()

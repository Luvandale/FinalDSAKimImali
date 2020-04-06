import pygame

#  Initialise pygame
pygame.init()

# Creating the Game window
gameWindow = pygame.display.set_mode((800, 600))

# Adding a Game Title
pygame.display.set_caption("Alien Shooter Game")
# Icon for the game
gameIcon = pygame.image.load('rocket.png')
pygame.display.set_icon(gameIcon)

# Defining Player Image and Starting Position of the player
playerIcon = pygame.image.load('space-invaders.png')
playerPosX = 360
playerPosY = 470


def playerCharacter():
    # the blit() method ois used to draw the player's Image icon at the defined positions for x and y
    gameWindow.blit(playerIcon, (playerPosX, playerPosY))


# Game Loop
# Makes sure the game window runs until the Quit button is pressed
gameRunning = True
while gameRunning is True:
    # Changing the game screen's background using RGB codes
    gameWindow.fill((0, 0, 255))

    # This for loop checks for the eventy that the quit button is
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    # Calling our Player to be displayed
    playerCharacter()
    # constantly updating our game window
    pygame.display.update()


import pygame
import random
from ColorPallet import *
pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Practice Snake Game')
#will be used to control frame rate of game
clock = pygame.time.Clock()

small_font = pygame.font.SysFont("comicsansms", 25)
med_font = pygame.font.SysFont("comicsansms", 50)
large_font = pygame.font.SysFont("comicsansms", 80)

def apple_spawn(apple_size): #inserting "block_size" as arguement currently
    #NOTE: the game only retains its grid-like structure if "display_width"
    # and "display_height" are both multiples of "apple_size"
    apple_x = round(random.randrange(0,display_width - apple_size)/apple_size) * apple_size
    apple_y = round(random.randrange(0,display_height - apple_size)/apple_size) * apple_size
    return apple_x, apple_y

#used to render the text ant the requested size of the text
def text_objects(text,color,size):
    if size == "small":
        textSurface = small_font.render(text,True,color)
    elif size == "medium":
        textSurface = med_font.render(text,True,color)
    elif size == "large":
        textSurface = large_font.render(text,True,color)
    return textSurface, textSurface.get_rect()

#used to display various messages to the user        
def message_to_user(msg, color, x_displace = 0, y_displace = 0, size = "small"):
    textSurface, textRect = text_objects(msg,color,size)
    #textRect is a list of 2 elements, the x coordinate and the y coordinate
    #of the message to render
    textRect.center = (display_width/2) + x_displace, (display_height/2) + y_displace
    gameDisplay.blit(textSurface, textRect)

#function used to keep score (we position score by topleft corner of
#text box instead of the center of the text box
def score(score):
    text = small_font.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0,0])
    
#define the start menue
def start_menue():
    starting = True
    while starting:
        gameDisplay.fill(white)
        message_to_user("Cedric's Snake Game",
                            green,
                            y_displace = -120,
                            size = "large")
        message_to_user("The objective of the game is to eat red apples",
                            black,
                            y_displace = -70)
        message_to_user("The more apple you eat, the longer you become",
                            black,
                            y_displace = -40)
        message_to_user("If you run into yourself, or the boundaries, you lose!",
                            black,
                            y_displace = -10)
        message_to_user("Press ENTER to play or ESC to quit",
                            black,
                            y_displace = 50)
        message_to_user("Controls: use the arrow keys to move and SPACE to pause the game",
                            black,
                            y_displace = 200)
        pygame.display.update()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    starting = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

def pause():
    paused = True
    return_to_start = False
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                if event.key == pygame.K_ESCAPE:
                    return_to_start = True
                    return return_to_start #used to return to start menue
##        gameDisplay.fill(white) #if we want to hide the game from the user while paused
        message_to_user("Paused",
                          black,
                          y_displace = -100,
                          size = 'large')
        message_to_user("Press SPACE to continue or ESCAPE to exit game",
                          black,
                          y_displace = 50,
                          size = 'small')
        pygame.display.update()
        clock.tick(15)

def game():
    
    gameActive = True
    gameOver = False

    #this list along with snakeLength controls the size of the snake
    snakeList = []
    snakeLength = 1

    block_size = 20 #use this to keep the game in a grid-like structure

    #initializes the placement of the snake
    place_x = display_width/2
    place_y = display_height/2
    move_x = 0
    move_y = -block_size #snake initially moving upwards

    #initializes the placement of the apple based on block size
    apple_x, apple_y = apple_spawn(block_size)

    while gameActive:

        #game over clause
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_user("Game Over",
                            red,
                            y_displace = -100,
                            size = "large")
            message_to_user("press SPACE to play again or ESC to exit",
                            black,
                            y_displace = 50)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        #remember: we added code that forces a quit
                        #within the start menue when certain user events occur
                        start_menue()
                        #NOTE: call the game again if the user quits
                        #one game and wants to start a new one
                        game()
                    if event.key == pygame.K_SPACE:
                        game()
                
        #main event hadler clause
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActive = False
            if event.type == pygame.KEYDOWN:
                #the extra "and" statement keeps the player from
                #backing the snake up into itself
                if event.key == pygame.K_LEFT and move_x != block_size:
                    move_x = -block_size
                    move_y = 0
                if event.key == pygame.K_RIGHT and move_x != -block_size:
                    move_x = block_size
                    move_y = 0
                if event.key == pygame.K_UP and move_y != block_size:
                    move_y = -block_size
                    move_x = 0
                if event.key == pygame.K_DOWN and move_y != -block_size:
                    move_y = block_size
                    move_x = 0
                if event.key == pygame.K_SPACE:
                    return_to_start = pause()
                    if return_to_start == True:
                        start_menue()
                        game()

        
        #updates coordinates of snake head
        place_x += move_x
        place_y += move_y

        #append updated coordinates to snake list, to create the entire snake body
        snakeHead = []
        snakeHead.append(place_x)
        snakeHead.append(place_y)
        snakeList.append(snakeHead)

        #renders the game board and the apple
        gameDisplay.fill(white)
        gameDisplay.fill(red,rect = [apple_x, apple_y, block_size, block_size])

        #keeps the snake from growing indefinitely
        if len(snakeList) > snakeLength:
            del snakeList[0]

        #check to see if the snake head has ran into its body: thus causing a game over
        for eachPart in snakeList[:-1]:
            if eachPart == snakeHead:
                gameOver = True

        #renders the snake's body on each frame
        for eachPart in snakeList:
            gameDisplay.fill(blue, rect = [eachPart[0], eachPart[1], block_size, block_size])

        #keeps the score
        score(snakeLength-1)
        
        #DONT FORGET TO UPDATE DISPLAY
        pygame.display.update()

        #checks to see if the snake head has ran into the boundaries of the game board
        if place_x < 0 or place_x >= display_width - block_size or place_y < 0 or place_y >= display_height - block_size:
            gameOver = True

        #updates the placement of the apple and the size of the snake body for
        #each apple eaten
        if apple_x == place_x and apple_y == place_y:
            apple_x, apple_y = apple_spawn(block_size)
            snakeLength += 1

        #controls the frame rate of the game
        clock.tick(15)
                

    pygame.quit()

#run start menue
start_menue()
#runs the game
game()
quit()

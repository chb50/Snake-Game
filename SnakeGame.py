import pygame
import random
from ColorPallet import *
pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Practice Snake Game')

font = font = pygame.font.SysFont(None, 25)

def message_to_user(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])


def game():
    
    gameActive = True
    gameOver = False

    #this list along with snakeLength controls the size of the snake
    snakeList = []
    snakeLength = 1

    #initializes the placement of the snake
    place_x = display_width/2
    place_y = display_height/2
    move_x = 0
    move_y = 0

    block_size = 10 #use this to keep the game in a grid-like structure

    #initializes the placement of the apple based on block size
    apple_x = round(random.randrange(0,display_width - block_size)/10.0) * 10.0
    apple_y = round(random.randrange(0,display_height - block_size)/10.0) * 10.0

    #will be used to control frame rate of game
    clock = pygame.time.Clock()

    while gameActive:

        #game over clause
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_user("Game Over: press C to continue or ESC to exit",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameActive = False
                        gameOver = False
                    if event.key == pygame.K_c:
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
    ##        if event.type == pygame.KEYUP:
    ##            #right now, if opposite keys are heald down and
    ##            #one of those keys are released, then the rectangle
    ##            #stops in place
    ##            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    ##                move_x = 0
    ##            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
    ##                move_y = 0
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

        #DONT FORGET TO UPDATE DISPLAY
        pygame.display.update()

        #checks to see if the snake head has ran into the boundaries of the game board
        if place_x < 0 or place_x >= display_width - block_size or place_y < 0 or place_y >= display_height - block_size:
            gameOver = True

        #updates the placement of the apple and the size of the snake body for
        #each apple eaten
        if apple_x == place_x and apple_y == place_y:
            apple_x = round(random.randrange(0,display_width - block_size)/10.0) * 10.0
            apple_y = round(random.randrange(0,display_height - block_size)/10.0) * 10.0
            snakeLength += 1

        #controls the frame rate of the game
        clock.tick(15)
                

    pygame.quit()

#runs the game
game()

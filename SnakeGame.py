import sqlite3
import pygame
import random
from SnakeGameProperties import *
from SnakeGameFunctions import *
pygame.init()

pygame.display.set_caption('Cedric\'s Snake Game')

def game():

    #Flags
    gameActive = True
    gameOver = False
    updatedHighScore = False

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
            
            if testHighScores(snakeLength - 1):
                message_to_user("New Hi Score!",
                                blue,
                                size = "medium")
                userTextInput(15, "small", white, y_displace = 50)
                
            message_to_user("press SPACE to play again or ESC to exit",
                            black,
                            y_displace = 100)
            pygame.display.update()
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        #remember: we added code that forces a quit
                        #within the start menue when certain user events occur
                        start_menu()
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
                        start_menu()
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

clearDB()
#run start menue
start_menu()
#runs the game
game()
quit()

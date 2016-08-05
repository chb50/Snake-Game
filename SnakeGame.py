### THIS IS THE MAIN FILE, THE GAME SHOULD BE RAN FROM HERE ###

import sqlite3
import pygame
import random
from SnakeGameProperties import *
from SnakeGameFunctions import *
from SnakeGameClasses import *

pygame.init()

pygame.display.set_caption('Cedric\'s Snake Game')

#define the start menue
def start_menu():
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
        message_to_user("Controls: use the arrow keys to move and SPACE to pause the ",
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
                    
def singlePlayerClassicGame():

    #Flags
    gameActive = True
    gameOver = False
    updatedHighScore = False

    block_size = 20 #use this to keep the game in a grid-like structure

    #NOTE: the block size for the apple should be the same as the snake
    playerSnake = Snake([], 1, block_size,
                        display_width/2, display_width/2, 0, -block_size, blue)

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
            #test and set high scores
            if testHighScores(playerSnake.snakeLength - 1) and updatedHighScore == False:
                hiScore = playerSnake.snakeLength - 1
                    
                message_to_user("New Hi Score!",
                                blue,
                                size = "medium")
                #get name from user
                username = userTextInput(15, "small", white, y_displace = 50)
                #place info into database
                setHighScores(username, hiScore)
                updatedHighScore = True
                
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
                        singlePlayerClassicGame()
                    if event.key == pygame.K_SPACE:
                        singlePlayerClassicGame()
                
        #main event hadler clause
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActive = False
            if event.type == pygame.KEYDOWN:
                #the extra "and" statement keeps the player from
                #backing the snake up into itself
                if event.key == pygame.K_LEFT and playerSnake.xVel != block_size:
                    playerSnake.xVel = -block_size
                    playerSnake.yVel = 0
                if event.key == pygame.K_RIGHT and playerSnake.xVel != -block_size:
                    playerSnake.xVel = block_size
                    playerSnake.yVel = 0
                if event.key == pygame.K_UP and playerSnake.yVel != block_size:
                    playerSnake.yVel = -block_size
                    playerSnake.xVel = 0
                if event.key == pygame.K_DOWN and playerSnake.yVel != -block_size:
                    playerSnake.yVel = block_size
                    playerSnake.xVel = 0
                if event.key == pygame.K_SPACE:
                    return_to_start = pause()
                    if return_to_start == True:
                        start_menu()
                        singlePlayerClassicGame()

        ## UPDATING THE SNAKE ON EVERY FRAME ##
                        
        #updates coordinates of snake head
        playerSnake.xCoord += playerSnake.xVel
        playerSnake.yCoord += playerSnake.yVel

        #append updated coordinates to snake list, to create the entire snake body
        snakeHead = []
        snakeHead.append(playerSnake.xCoord)
        snakeHead.append(playerSnake.yCoord)
        playerSnake.snakeList.append(snakeHead)

        #renders the game board and the apple
        gameDisplay.fill(white)
        gameDisplay.fill(red,rect = [apple_x, apple_y, playerSnake.blockSize, playerSnake.blockSize])

        #keeps the snake from growing indefinitely
        if len(playerSnake.snakeList) > playerSnake.snakeLength:
            del playerSnake.snakeList[0]

        #check to see if the snake head has ran into its body: thus causing a game over
        for eachPart in playerSnake.snakeList[:-1]:
            if eachPart == snakeHead:
                gameOver = True

        #renders the snake's body on each frame
        for eachPart in playerSnake.snakeList:
            gameDisplay.fill(playerSnake.color, rect = [eachPart[0], eachPart[1], playerSnake.blockSize, playerSnake.blockSize])

        #keeps the score
        score(playerSnake.snakeLength-1)
        
        #DONT FORGET TO UPDATE DISPLAY
        pygame.display.update()

        #checks to see if the snake head has ran into the boundaries of the game board
        if playerSnake.xCoord < 0 or playerSnake.xCoord >= display_width - playerSnake.blockSize or playerSnake.yCoord < 0 or playerSnake.yCoord >= display_height - playerSnake.blockSize:
            gameOver = True

        #updates the placement of the apple and the size of the snake body for
        #each apple eaten
        if apple_x == playerSnake.xCoord and apple_y == playerSnake.yCoord:
            apple_x, apple_y = apple_spawn(playerSnake.blockSize)
            playerSnake.snakeLength += 1

        #controls the frame rate of the game
        clock.tick(15)
                

    pygame.quit()

## FOR TESTING ONLY ##
##clearDB()


#run start menue
start_menu()
#runs the game
singlePlayerClassicGame()
quit()

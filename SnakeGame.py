### THIS IS THE MAIN FILE, THE GAME SHOULD BE RAN FROM HERE ###

import sqlite3
import pygame
import random
from SnakeGameProperties import *
from SnakeGameFunctions import *
from SnakeGameClasses import *

pygame.init()

pygame.display.set_caption('Cedric\'s Snake Game')
                    
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
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        #remember: we added code that forces a quit
                        #within the start menue when certain user events occur
                        start_menu()
                    if event.key == pygame.K_SPACE:
                        singlePlayerClassicGame()
                
        #main event hadler clause, controls are arrow keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActive = False
            if event.type == pygame.KEYDOWN:
                #the extra "and" statement keeps the player from
                #backing the snake up into itself
                if event.key == pygame.K_LEFT and playerSnake.xVel != playerSnake.blockSize:
                    playerSnake.xVel = -block_size
                    playerSnake.yVel = 0
                if event.key == pygame.K_RIGHT and playerSnake.xVel != -playerSnake.blockSize:
                    playerSnake.xVel = block_size
                    playerSnake.yVel = 0
                if event.key == pygame.K_UP and playerSnake.yVel != playerSnake.blockSize:
                    playerSnake.yVel = -block_size
                    playerSnake.xVel = 0
                if event.key == pygame.K_DOWN and playerSnake.yVel != -playerSnake.blockSize:
                    playerSnake.yVel = block_size
                    playerSnake.xVel = 0
                if event.key == pygame.K_SPACE:
                    return_to_start = pause()
                    if return_to_start == True:
                        start_menu()

        ## UPDATING THE SNAKE ON EVERY FRAME ##

        #renders the game board and the apple
        gameDisplay.fill(white)
        gameDisplay.fill(red,rect = [apple_x, apple_y, playerSnake.blockSize, playerSnake.blockSize])

        #update the movement of the snake for this frame
        playerSnake.snakeMovement()

        #renders the snake's body on each frame
        for eachPart in playerSnake.snakeList:
            gameDisplay.fill(playerSnake.color, rect = [eachPart[0], eachPart[1], playerSnake.blockSize, playerSnake.blockSize])

        ## GAME SPECIFIC RULES ##
        ## design choice: did not want to include a function for this in the snake class ##
        ## because the rules of the game may change for future game types I may implement ##
        
        #check to see if the snake head has ran into its body: thus causing a game over
        for eachPart in playerSnake.snakeList[:-1]:
            if eachPart == playerSnake.snakeHead:
                gameOver = True

        #checks to see if the snake head has ran into the boundaries of the game board
        if playerSnake.xCoord < 0 or playerSnake.xCoord >= display_width - playerSnake.blockSize or playerSnake.yCoord < 0 or playerSnake.yCoord >= display_height - playerSnake.blockSize:
            gameOver = True

        #updates the placement of the apple and the size of the snake body for
        #each apple eaten
        if apple_x == playerSnake.xCoord and apple_y == playerSnake.yCoord:
            apple_x, apple_y = apple_spawn(playerSnake.blockSize)
            playerSnake.snakeLength += 1

        #keeps the score
        score(playerSnake.snakeLength-1)
        
        #DONT FORGET TO UPDATE DISPLAY
        pygame.display.update()

        #controls the frame rate of the game
        clock.tick(15)
                

def twoPlayerGame():

    #TODO: figure out what to do when the snakes colide head on with each other

    #Flags
    gameActive = True
    gameOver = False
    playerWon = 0

    blockSize = 20
    #game will be based on who kills who
    #an apple will spawn and each player has to eat the apple to grow
    playerOne = Snake([], 1, blockSize, 100, 340, 0, -blockSize, blue)
    playerTwo = Snake([], 1, blockSize, 700, 60, 0, blockSize, green)

    #initial apple placement will be in center
    appleX = display_width/2
    appleY = display_height/2

    while gameActive:

        while gameOver:
            
            gameDisplay.fill(white)
            message_to_user("Game Over",
                            red,
                            y_displace = -100,
                            size = "large")
            message_to_user("Player " + str(playerWon) + " won!",
                            blue,
                            size = "medium")
            message_to_user("press SPACE to play again or ESC to exit",
                            black,
                            y_displace = 100)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False
                    gameOver = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        #remember: we added code that forces a quit
                        #within the start menue when certain user events occur
                        start_menu()
                    if event.key == pygame.K_SPACE:
                        twoPlayerGame()
            

        #playerMovement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActive = False
            if event.type == pygame.KEYDOWN:
                #the extra "and" statement keeps the player from
                #backing the snake up into itself
                #player one
                if event.key == pygame.K_a and playerOne.xVel != blockSize:
                    playerOne.xVel = -blockSize
                    playerOne.yVel = 0
                if event.key == pygame.K_d and playerOne.xVel != -blockSize:
                    playerOne.xVel = blockSize
                    playerOne.yVel = 0
                if event.key == pygame.K_w and playerOne.yVel != blockSize:
                    playerOne.yVel = -blockSize
                    playerOne.xVel = 0
                if event.key == pygame.K_s and playerOne.yVel != -blockSize:
                    playerOne.yVel = blockSize
                    playerOne.xVel = 0
                #player two
                if event.key == pygame.K_j and playerTwo.xVel != blockSize:
                    playerTwo.xVel = -blockSize
                    playerTwo.yVel = 0
                if event.key == pygame.K_l and playerTwo.xVel != -blockSize:
                    playerTwo.xVel = blockSize
                    playerTwo.yVel = 0
                if event.key == pygame.K_i and playerTwo.yVel != blockSize:
                    playerTwo.yVel = -blockSize
                    playerTwo.xVel = 0
                if event.key == pygame.K_k and playerTwo.yVel != -blockSize:
                    playerTwo.yVel = blockSize
                    playerTwo.xVel = 0
                #pause
                if event.key == pygame.K_SPACE:
                    return_to_start = pause()
                    if return_to_start == True:
                        start_menu()
                        
        #renders the game board and the apple
        gameDisplay.fill(white)
        gameDisplay.fill(red,rect = [appleX, appleY, blockSize, blockSize])

        #update player movement
        playerOne.snakeMovement()
        playerTwo.snakeMovement()

        #render snakes
        for eachPart in playerOne.snakeList:
            gameDisplay.fill(playerOne.color, rect = [eachPart[0], eachPart[1], playerOne.blockSize, playerOne.blockSize])

        for eachPart in playerTwo.snakeList:
            gameDisplay.fill(playerTwo.color, rect = [eachPart[0], eachPart[1], playerTwo.blockSize, playerTwo.blockSize])

        #check to see if the snake head has ran into its body: thus causing a game over
        for eachPart in playerOne.snakeList[:-1]:
            #tests if snake runs into itself
            if eachPart == playerOne.snakeHead:
                playerWon = 2
                gameOver = True
            #tests if player 2's snake runs into player 1's snake
            if eachPart == playerTwo.snakeHead:
                playerWon = 1
                gameOver = True

        for eachPart in playerTwo.snakeList[:-1]:
            if eachPart == playerTwo.snakeHead:
                playerWon = 1
                gameOver = True
            if eachPart == playerOne.snakeHead:
                playerWon = 2
                gameOver = True

        #checks to see if the snake head has ran into the boundaries of the game board
        if playerOne.xCoord < 0 or playerOne.xCoord >= display_width - playerOne.blockSize or playerOne.yCoord < 0 or playerOne.yCoord >= display_height - playerOne.blockSize:
            playerWon = 2
            gameOver = True

        if playerTwo.xCoord < 0 or playerTwo.xCoord >= display_width - playerTwo.blockSize or playerTwo.yCoord < 0 or playerTwo.yCoord >= display_height - playerTwo.blockSize:
            playerWon = 1
            gameOver = True

        #updates the placement of the apple and the size of the snake body for
        #each apple eaten
        if appleX == playerOne.xCoord and appleY == playerOne.yCoord:
            appleX, appleY = apple_spawn(playerOne.blockSize)
            playerOne.snakeLength += 1

        if appleX == playerTwo.xCoord and appleY == playerTwo.yCoord:
            appleX, appleY = apple_spawn(playerTwo.blockSize)
            playerTwo.snakeLength += 1

        #DONT FORGET TO UPDATE DISPLAY
        pygame.display.update()

        #controls the frame rate of the game
        clock.tick(15)
    
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
                    #runs the game
                    starting = False
                    #singlePlayerClassicGame()
                    twoPlayerGame()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

## FOR TESTING ONLY ##
##clearDB()

#run start menue
start_menu()

quit()

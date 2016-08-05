#classes to describe sprites of game
import pygame

class Snake(object):
    def __init__(self, snakeList, snakeLength, blockSize,
                 xCoord, yCoord, xVel, yVel, color, img = None):
        #use this list to append blocks together that forms the snake
        self.snakeList = snakeList
        
        #integer which tracks the length of the snake
        self.snakeLength = snakeLength
        
        #size of each block that makes the snake
        self.blockSize = blockSize
        
        #horizonatal position of the snake
        self.xCoord = xCoord
        
        #verticle position of the snake
        self.yCoord = yCoord
        
        #horizontal velocity of the snake
        self.xVel = xVel
        
        #verticle velocity of the snake
        self.yVel = yVel
        
        #color of the snake
        self.color = color
        
        #a png that could be used as the head of the snake
        self.img = img

        #keeps track of how the snake should move based on user input
        #appended to snakeList so the snake's position is updated on each frame
        self.snakeHead = []

    def snakeMovement(self):
        #create new coordinates based on velocities (user input)
        self.xCoord += self.xVel
        self.yCoord += self.yVel
        
        #update snake head with new coordinants based on user input
        self.snakeHead = []
        self.snakeHead.append(self.xCoord)
        self.snakeHead.append(self.yCoord)
        self.snakeList.append(self.snakeHead)

        #updates display to keep the snake at the correct size, rather
        #than growing it indefinitely
        if len(self.snakeList) > self.snakeLength:
            del self.snakeList[0]

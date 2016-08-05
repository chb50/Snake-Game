#classes to describe sprites of game

class Snake(object):
    def __init__(snakeList, snakeLength, snakeBlockSize
                 xCoord, yCoord, xVel, yVel, color, img = None):
        #use this list to append blocks together that forms the snake
        self.snakeList = snakeList
        
        #integer which tracks the length of the snake
        self.snakeLength = snakeLength
        
        #size of each block that makes the snake
        self.snakeBlockSize = snakeBlockSize
        
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

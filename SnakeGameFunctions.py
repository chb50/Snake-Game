import pygame
import random
import sqlite3
import datetime
import time
from SnakeGameProperties import *

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

#compare current score with scores stored within the database
def testHighScores(score):
    #Table will have: rank, name, date, score
    connect = sqlite3.connect("SnakeGameDatabase.db")
    c = connect.cursor()

    c.execute('SELECT * FROM highScores')

    for row in c.fetchall():
        if score > row[3]:
            c.close()
            connect.close()
            return True

    c.close()
    connect.close()
    return False

#returns true if high score is achieved, false otherwise
#TODO: this code will have to change such that the user will input a name only when their score is confirmed to be a high score (from the function above)
def setHighScores(name, score):
    connect = sqlite3.connect("SnakeGameDatabase.db")
    c = connect.cursor()

    date = str(datetime.datetime.fromtimestamp(time.time()).strftime('%m-%d-%Y %H:%M'))
    isHighScore = False
    maxTableSize = 5 #maximum # of high scores allowed on the table
    rank = 1
    
    c.execute('CREATE TABLE IF NOT EXISTS highScores(rank INT, name TEXT, datestamp TEXT, score INT)')
    c.execute('SELECT COUNT(*) FROM highScores')
    currentSize = c.fetchone()[0] #should get the current table's size

    if currentSize == 0:
        c.execute('INSERT INTO highScores (rank, name, datestamp, score) VALUES (?, ?, ?, ?)',
                  (rank, name, date, score))
        connect.commit()
        c.close()
        connect.close()
        return True
    else:
        prevRow = None
        c.execute('SELECT * FROM highScores')
        for row in c.fetchall():
            if score > row[3]:
                isHighScore = True
                #add the data to the table
                prevRow = row
                c.execute('UPDATE highScores SET name = ?, datestamp = ?, score = ? WHERE rank = ?',
                          (name, date, score, rank))
                connect.commit()
                #will need to push rows with lower score down, so we save the past high score to be placed in the row below
                if rank >= maxTableSize:
                    #if the max table size has been reached, disregard the lowest score (prevRow)
                    c.close()
                    connect.close()
                    return True
                name = prevRow[1]
                date = prevRow[2]
                score = prevRow[3]
            rank += 1
    print(rank)
    #if the for loop ends, then this means one of 2 things:
    #   1)the maximum rank allowed on the table was not reached,therefore, we need to insert the info of the lowest score on the high score board (prevRow)
        #either the score has been inserted, and we need to move older high scores down
        #or this score is the smallest of all scores, and we need to insert it below the previous lowest score
    #   2)the score delivered as arguement to this function is lower than the lowest high score

    if rank <= maxTableSize:
        #name, date, score will come from either prevRow or current player that earned this high score spot
        c.execute('INSERT INTO highScores (rank, name, datestamp, score) VALUES (?, ?, ?, ?)',
              (rank, name, date, score))
        connect.commit()
        c.close()
        connect.close()
        return True
    else:        
        c.close()
        connect.close()
        return False


    ## Have to account for
    #   1) adding a row to an empty table
    #   2) adding a row to a table that is currently not the maximum size allowed
    #       will need to be able to save previous scores such that they can be moved down on the high score list
    #   3) adding a row to a table that is the maximum size allowed
    #       will have to delete the last member of the list of old high scores to make room for the new high score
    #   4) not adding to the table (the score is too low)

### ONLY FOR TESTING ###
def clearDB():
    connect = sqlite3.connect("SnakeGameDatabase.db")
    c = connect.cursor()

    c.execute("DELETE FROM highScores")
    connect.commit()

    c.close()
    connect.close()


    
    

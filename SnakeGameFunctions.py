import pygame
import random
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

#Script describing the properties of Snake
import pygame
pygame.init()

#Color Pallet
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
gray = (145, 145, 145)

#Fonts
small_font = pygame.font.SysFont("comicsansms", 25)
med_font = pygame.font.SysFont("comicsansms", 50)
large_font = pygame.font.SysFont("comicsansms", 80)

#display
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock() #will be used to control frame rate of game

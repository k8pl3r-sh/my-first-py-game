#!/bin/python3

# pip install pygame, pygame-menu

# Imports
import sys # for quitting the script to avoid IDE bug
import random, time
import pygame
from pygame.locals import * # avoid using pygame.locals prefix

pygame.init()  # initialize pygame engine


# Create our colors for the game: predefined colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Configure FPS: (by default, execute the loop as many time as possible-> too much fluctuations)
FPS = 60
FramePerSec = pygame.time.Clock()

# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Variables
SPEED = 5
SCORE = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
background = pygame.image.load("AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # Window of fixed size
# top-left corner is the coordinates (0, 0), and bottom right corner is (300,300) in our case
# customize window later (changing title and default icon): https://coderslegacy.com/python/how-to-change-the-pygame-icon/
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Highway run") #Title of the window


#### Classes ###
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) # randomized starting points
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
      #def draw(self, surface):
        #surface.blit(self.image, self.rect) 
 
 
class Player(pygame.sprite.Sprite):  # argument makes the class a child
    def __init__(self):
        super().__init__() # calls the init function of the Sprite class
        self.image = pygame.image.load("Player.png") # Load image
        self.rect = self.image.get_rect() #set the borders (rectangle of the same size as the image)
        self.rect.center = (160, 520) # Defines the starting position for the Rect
        # Be carreful or we can have image and Rect at a different place
 
    def move(self): # method from the player class
        pressed_keys = pygame.key.get_pressed()
       # We don't need up and down movement there
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0: 
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
        # self.rect.left > 0 and self.rect.right < SCREEN WIDTH ensure that the player is not off the screen

    #def draw(self, surface):
        #surface.blit(self.image, self.rect) #2 input: surface  and rect (here surf=img)
        # Surfaces article creation: https://coderslegacy.com/python/pygame-surface/     

# Setting up Sprites
P1 = Player()
E1 = Enemy()

# Creating Sprites groups: sort of like classification
enemies = pygame.sprite.Group() # ennemy group
enemies.add(E1) # use add() to add sprite
all_sprites = pygame.sprite.Group() # group for all
all_sprites.add(P1)
all_sprites.add(E1)

#Adding a new User event
INC_SPEED = pygame.USEREVENT + 1 # user event to increase difficulty
pygame.time.set_timer(INC_SPEED, 1000) # call the INC_SPEED event every 1s


# pygame mixer
pygame.mixer.music.load('background.wav') # load the music (then play it with: pygame.mixer.music.play(-1))
# -1 indefinitely; 0 or nothing: once;  x times -> repeated x times
# pygame.mixer.music.stop() to stop the music

### Game loop ###
while True:
    for event in pygame.event.get(): # catch all events
        if event.type == INC_SPEED:
              SPEED += 2              
        if event.type == QUIT:
            pygame.quit() # Close pygame window
            sys.exit() # Close python script
    
    pygame.mixer.music.play(-1)
    #DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))


    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect) # interest of grouping: move and redraw in 3 lines
        entity.move()

 
    #To be run if collision occurs between Player and Enemy: COLLISIONS
    if pygame.sprite.spritecollideany(P1, enemies): #function to check collision btw a sprite and sprite group
            pygame.mixer.music.stop()
            pygame.mixer.Sound('crash.wav').play()
            time.sleep(0.5)

            DISPLAYSURF.fill(RED) # Fill the screen with red if collision
            DISPLAYSURF.blit(game_over, (30,250))

            pygame.display.update()
            for entity in all_sprites:
                entity.kill() #remove the sprite from the group
            time.sleep(2)
            pygame.quit()
            sys.exit()
         
    pygame.display.update() # Changes are not implemented until this
    FramePerSec.tick(FPS)




### DOCUMENTATION ###
# pygame event when a user performs a specific action: create custom events: https://coderslegacy.com/python/pygame-userevents/

# attributes of an object: type,...

# pygame colors: RGB: 256x256x256=16 millions

# Rects and collision detection:
# collision of entities -> attack/... https#://coderslegacy.com/python/pygame-rect-tutorial/
""" Example code to  check collisions
object1 = pygame.Rect((20, 50), (50, 100))
object2 = pygame.Rect((10, 10), (100, 100))
 
print(object1.colliderect(object2))
"""
# There is another trick we can use to automatically create a Rect based off an image’s dimensions. We will explore this later on in this Pygame tutorial.


# Optimize and speed up the game: https://coderslegacy.com/improving-speed-performance-in-pygame/

# Classes are very important to avoid rebuilding every elements

# Fonts use the file .ttf, which stands for True Type File: https://coderslegacy.com/python/pygame-font/

# STEPS:
# 0 - Brainstorm the idea to have clear steps and needs
# 1 - Initialize the code, and architecture of the project (script + folders ...), nomenclature TODO etc...
# 2 - Build the game, classes and methods
# 3 - Add background, sound, fonts, scoring ...
# 4 - Optimize


# TODO: 
# multiple ennemy spawning after a certain period of time (similar to how we increase speed after a set period of time)
# Adding audio: background (DONE), movement sound
# Multiple lives
# Variations in the shape and size of the ennemy & multiples subclasses (trucks...)

# Me: Menu to restart/quit the game
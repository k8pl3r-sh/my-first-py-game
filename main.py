#!/bin/python3
import sys # for quitting the script to avoid IDE bug
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
FPS = pygame.time.Clock()
FPS.tick(60)

# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((300,300)) # Window of fixed size
# top-left corner is the coordinates (0, 0), and bottom right corner is (300,300) in our case

# customize window later (changing title and default icon): https://coderslegacy.com/python/how-to-change-the-pygame-icon/
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")






### Game loop ###
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
 
      def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 
 
 
class Player(pygame.sprite.Sprite):  # argument makes the class a child
    def __init__(self):
        super().__init__() # calls the init function of the Sprite class
        self.image = pygame.image.load("Player.png") # Load image
        self.rect = self.image.get_rect() #set the borders (rectangle of the same size as the image)
        self.rect.center = (160, 520) # Defines the starting position for the Rect
        # Be carreful or we can have image and Rect at a different place
 
    def update(self): # method from the player class
        pressed_keys = pygame.key.get_pressed()
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
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)     
 
         
P1 = Player()
E1 = Enemy()
 
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit() # Close pygame window
            sys.exit() # Close python script
    P1.update()
    E1.move()
     
    DISPLAYSURF.fill(WHITE)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
         
    pygame.display.update() # Changes are not implemented until this




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

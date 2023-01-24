from time import sleep
import pygame, random, time
import pygame_menu
from pygame_menu import themes
from pygame.locals import *
 
pygame.init()
surface = pygame.display.set_mode((400, 600))
 
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
pygame.display.set_caption("Game") #Title of the window


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


def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)
 
def start_the_game():
    pass
 
def level_menu():
    mainmenu._open(level)
 
 
mainmenu = pygame_menu.Menu('Welcome', 400, 600, theme=themes.THEME_SOLARIZED)
mainmenu.add.text_input('Name: ', default='username', maxchar=20)
mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Levels', level_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)
 
level = pygame_menu.Menu('Select a Difficulty', 400, 600, theme=themes.THEME_BLUE)
level.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
 
# mainmenu.mainloop(surface)
# Can be replaced by:

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
 
    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)
 
    pygame.display.update()
    FramePerSec.tick(FPS)
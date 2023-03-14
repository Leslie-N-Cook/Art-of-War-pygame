"""
    Author:   Byron Dowling
    Class:    5443 2D Python Gaming

    Asset Credits:

        - Viking Sprites:
            - Author: [Ragewortt]
            - https://ragewortt.itch.io/fantasy-heroes-vikinself.image-sprite-sheet

        - Pirate Sprites:
            - Author: [Free Game Assets]
            - https://free-game-assets.itch.io/free-2d-pirate-sprites

        - Knight Sprites:
            - Author: [Free Game Assets]
            - https://free-game-assets.itch.io/free-2d-knight-sprite-sheets

        Background Art:
            - [Author] "klyaksun"
            - https://www.vecteezy.com/vector-art/15370321-ancient-roman-arena-for-gladiators-fight
            - https://www.vecteezy.com/vector-art/13852032-ancient-roman-arena-for-gladiators-fight-at-night

"""

import pygame
import pprint
import os
import utilities
import PlayerSelection
#from PlayerSelection import PlayerSelector
from PIL import Image, ImageDraw


###################################################################################################

"""
 ██████╗  █████╗  ██████╗██╗  ██╗ ██████╗ ██████╗  ██████╗ ██╗   ██╗███╗   ██╗██████╗ 
 ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝ ██╔══██╗██╔═══██╗██║   ██║████╗  ██║██╔══██╗
 ██████╔╝███████║██║     █████╔╝ ██║  ███╗██████╔╝██║   ██║██║   ██║██╔██╗ ██║██║  ██║
 ██╔══██╗██╔══██║██║     ██╔═██╗ ██║   ██║██╔══██╗██║   ██║██║   ██║██║╚██╗██║██║  ██║
 ██████╔╝██║  ██║╚██████╗██║  ██╗╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝ 
                                                                                      
 ██╗███╗   ███╗ █████╗  ██████╗ ███████╗██████╗ ██╗   ██╗                             
 ██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝██╔══██╗╚██╗ ██╔╝                             
 ██║██╔████╔██║███████║██║  ███╗█████╗  ██████╔╝ ╚████╔╝                              
 ██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝  ██╔══██╗  ╚██╔╝                               
 ██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗██║  ██║   ██║                                
 ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝                                


      Helper background class from Dr. Griffin used on Batteship demo                                                                                 
"""

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):

        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.width, self.height = self.getImgWidthHeight(image_file)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (1400, 750))

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
        


    def getImgWidthHeight(self, path):
        """Uses pil to image size in pixels.
        Params:
            path (string) : path to the image
        """
        if os.path.isfile(path):
            im = Image.open(path)
            return im.size
        return None


###################################################################################################

"""
 
  ██████╗  █████╗ ███╗   ███╗███████╗        
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝        
 ██║  ███╗███████║██╔████╔██║█████╗          
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝          
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗        
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝        
                                             
 ███████╗██████╗ ██████╗ ██╗████████╗███████╗
 ██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝██╔════╝
 ███████╗██████╔╝██████╔╝██║   ██║   █████╗  
 ╚════██║██╔═══╝ ██╔══██╗██║   ██║   ██╔══╝  
 ███████║██║     ██║  ██║██║   ██║   ███████╗
 ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝
                                             
"""

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, imgLink, location, smsc_dimensions, inverted=False):
        self.location = location
        
        self.image = self.__makeImage(imgLink, smsc_dimensions, inverted)
            
        self.rect = self.image.get_rect(topleft = location)
        
    def draw(self):
        # pygame.draw.rect(screen, (255,0,0), self.rect)
        
        screen.blit(self.image, self.rect.topleft)
        
    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
        
    def changeImage(self, imgLink, smsc_dimensions, inverted=False):
        self.image = self.__makeImage(imgLink, smsc_dimensions, inverted)
        
    def __makeImage(self, imgLink, smsc_dimensions, inverted=False):
        if not inverted:
            image = pygame.image.load(imgLink)
            image = pygame.transform.smoothscale(image, smsc_dimensions)

        ## Inverted case where the Sprite is facing left
        else:
            image = pygame.image.load(imgLink)
            image = pygame.transform.smoothscale(image, smsc_dimensions)
            image_Copy = image.copy()
            image = pygame.transform.flip(image_Copy, True, False)
            
        return image
        
###################################################################################################

"""
  ██████╗  █████╗ ███╗   ███╗███████╗                                
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝                                
 ██║  ███╗███████║██╔████╔██║█████╗                                  
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝                                  
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗                                
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝                                
                                                                     
 ██╗   ██╗ █████╗ ██████╗ ██╗ █████╗ ██████╗ ██╗     ███████╗███████╗
 ██║   ██║██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗██║     ██╔════╝██╔════╝
 ██║   ██║███████║██████╔╝██║███████║██████╔╝██║     █████╗  ███████╗
 ╚██╗ ██╔╝██╔══██║██╔══██╗██║██╔══██║██╔══██╗██║     ██╔══╝  ╚════██║
  ╚████╔╝ ██║  ██║██║  ██║██║██║  ██║██████╔╝███████╗███████╗███████║
   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚══════╝                                                                   
 """


## Rough Dimensions of Byron's Monitor
screenWidth = 1400
screenHeight = 750

## Set the size of the window using the above dimensions
size = (screenWidth, screenHeight)
screen = pygame.display.set_mode(size)

## Setting the background image and orienting starting from (0,0) origin i.e top left corner
# BackGround = Background("Arena.jpg", [0, 0])
BackGround = Background("Arena_Night.png", [0, 0])
middle = pygame.Rect((screenWidth/2)-5, 0, 10, screenHeight)
## Pseudo-random character selection
C4 = PlayerSelection.PlayerSelector()
sprites = C4.chooseSprites()
P1 = sprites[0]
P2 = sprites[1]

P1_idle_frameCount = P1["Action"]["Idle"]["frameCount"]
P1_idle_frame = 0
P1_name = P1["Screen Name"]

P2_idle_frameCount = P2["Action"]["Idle"]["frameCount"]
P2_idle_frame = 0
P2_name = P2["Screen Name"]

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(sprites)


## Set the title of the window
banner = f'Get Ready for Deadliest Warrior! {P1_name} vs {P2_name}'
pygame.display.set_caption(banner)


tick = 5
#frames per second
FPS = 60
#velocity
velocity = .5

left_hit = pygame.USEREVENT + 1
right_hit = pygame.USEREVENT + 2
clock = pygame.time.Clock()
        
  ## Spawn player sprites
P1_link = f'{P1["Action"]["Idle"]["imagePath"]}/{P1_idle_frame}.png'
Player1 = GameSprite(P1_link, (70,400), (250,250), False)

P2_link = f'{P2["Action"]["Idle"]["imagePath"]}/{P2_idle_frame}.png'
Player2 = GameSprite(P2_link, (1100,400), (250,250), True)
########################################################################################

"""
  ██████╗  █████╗ ███╗   ███╗███████╗    ██╗      ██████╗  ██████╗ ██████╗ 
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██║     ██╔═══██╗██╔═══██╗██╔══██╗
 ██║  ███╗███████║██╔████╔██║█████╗      ██║     ██║   ██║██║   ██║██████╔╝
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║     ██║   ██║██║   ██║██╔═══╝ 
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ███████╗╚██████╔╝╚██████╔╝██║     
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝                                                                             
"""

## Run the game loop

## Initialize Pygame
pygame.init()
running = True

pygame.mixer.init()
utilities.background_music()

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        
    keys_pressed = pygame.key.get_pressed()       
    if keys_pressed[pygame.K_a]:
        Player1.move(-1,0)
    if keys_pressed[pygame.K_d]:
        Player1.move(1,0)
    if keys_pressed[pygame.K_w]:
        Player1.move(0,-1)
    if keys_pressed[pygame.K_s]:
        Player1.move(0,1)
        
    if keys_pressed[pygame.K_LEFT]:
        Player2.move(-1,0)
    if keys_pressed[pygame.K_RIGHT]:
        Player2.move(1,0)
    if keys_pressed[pygame.K_UP]:
        Player2.move(0,-1)
    if keys_pressed[pygame.K_DOWN]:
        Player2.move(0,1)

    ## "I want you to paint it, paint it, paint it black"
    ## 0,0,0 is default black background
    screen.fill((0,0,0))

    ## Layering background image of map imagery
    screen.blit(BackGround.image, BackGround.rect)
    right_health = 10
    left_health = 10
    Health_font = pygame.font.Font('font/Algerian.ttf', 40)
    right_health_text = Health_font.render(
            "Health: " + str(right_health), 1, (255,255,255))
    left_health_text = Health_font.render(
            "Health: " + str(left_health), 1, (255,255,255))
    screen.blit(right_health_text, (screenWidth - right_health_text.get_width() - 10, 10))
    screen.blit(left_health_text, (10, 10))
    
    if tick % 3 == 0:
        if P1_idle_frame < P1_idle_frameCount - 1:
            P1_idle_frame += 1
        else:
            P1_idle_frame = 0

        if P2_idle_frame < P2_idle_frameCount - 1:
            P2_idle_frame += 1
        else:
            P2_idle_frame = 0

    Player1.draw()
    Player2.draw()
    
    P1_link = f'{P1["Action"]["Idle"]["imagePath"]}/{P1_idle_frame}.png'
    P2_link = f'{P2["Action"]["Idle"]["imagePath"]}/{P2_idle_frame}.png'
    
    Player1.changeImage(P1_link, (250,250), False)
    Player2.changeImage(P2_link, (250,250), True)
  


    tick += 1

    pygame.display.update()

###################################################################################################


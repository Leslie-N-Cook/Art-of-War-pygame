"""
    Author:   Byron Dowling
    Class:    5443 2D Python Gaming

    Asset Credits:

        - Viking Sprites:
            - Author: [Ragewortt]
            - https://ragewortt.itch.io/fantasy-heroes-vikings-sprite-sheet

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
from PlayerSelection import PlayerSelector
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
        self.image = pygame.transform.scale(self.image, (2038, 862))

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

class GameSprite:
    def __init__(self, imgLink, location, smsc_dimensions, inverted=False):
        
        if not inverted:
            GS = pygame.image.load(imgLink)
            GS = pygame.transform.smoothscale(GS, smsc_dimensions)
            screen.blit(GS, location)

        ## Inverted case where the Sprite is facing left
        else:
            GS = pygame.image.load(imgLink)
            GS = pygame.transform.smoothscale(GS, smsc_dimensions)
            GS_Copy = GS.copy()
            IGS = pygame.transform.flip(GS_Copy, True, False)
            screen.blit(IGS, location)

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

## Initialize Pygame
pygame.init()
running = True

## Rough Dimensions of Byron's Monitor
screenWidth = 1750
screenHeight = 800

## Set the size of the window using the above dimensions
size = (screenWidth, screenHeight)
screen = pygame.display.set_mode(size)

## Setting the background image and orienting starting from (0,0) origin i.e top left corner
# BackGround = Background("Arena.jpg", [0, 0])
BackGround = Background("Arena_Night.jpg", [0, 0])

## Pseudo-random character selection
C4 = PlayerSelector()
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

tick = 0

###################################################################################################

"""
  ██████╗  █████╗ ███╗   ███╗███████╗    ██╗      ██████╗  ██████╗ ██████╗ 
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██║     ██╔═══██╗██╔═══██╗██╔══██╗
 ██║  ███╗███████║██╔████╔██║█████╗      ██║     ██║   ██║██║   ██║██████╔╝
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║     ██║   ██║██║   ██║██╔═══╝ 
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ███████╗╚██████╔╝╚██████╔╝██║     
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝                                                                             
"""

## Run the game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    ## "I want you to paint it, paint it, paint it black"
    ## 0,0,0 is default black background
    screen.fill((0,0,0))

    ## Layering background image of map imagery
    screen.blit(BackGround.image, BackGround.rect)

    if tick % 2 == 0:
        if P1_idle_frame < P1_idle_frameCount - 1:
            P1_idle_frame += 1
        else:
            P1_idle_frame = 0

        if P2_idle_frame < P2_idle_frameCount - 1:
            P2_idle_frame += 1
        else:
            P2_idle_frame = 0


    ## Spawn player sprites
    P1_link = f'{P1["Action"]["Idle"]["imagePath"]}\{P1_idle_frame}.png'
    Player1 = GameSprite(P1_link, (350,500), (250,250), False)

    P2_link = f'{P2["Action"]["Idle"]["imagePath"]}\{P2_idle_frame}.png'
    Player2 = GameSprite(P2_link, (1350,500), (250,250), True)


    tick += 1

    pygame.display.update()

###################################################################################################


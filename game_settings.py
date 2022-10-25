

import pygame 
import random 
# import os
# import torch 
# import torch.nn as nn 


# WINDOW 
GAME_WIDTH  = 700                                              
GAME_HEIGHT = 450   
WIN = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT))                      
pygame.init()
pygame.mixer.init()        

# COLORs
BLACK   = (0,0,0)
RED     = (255,0,0)      
YELLOW  = (255,255,0)    
PINK    = (255,192,203)  
WHITE   = (255,255,255)
COLOR_1 = (128,255,0)
COLOR_2 = (204,102,0)
COLOR_3 = (255,0,127)

# BIRDS 
BIRD_WIDTH  = 20
BIRD_HEIGHT = 20
BIRD_VEL    = 1.2
BIRD_JUMP   = 30
BIRD_FALL   = 1.5

# PILLARS 
PILLAR_WIDTH  = 50
PILLAR_HEIGHT = 200 
PILLAR_GAP    = 130
PILLARS_DIST  = 300








# SOUND
# BULLET_FIRED_SOUND = pygame.mixer.Sound(os.path.join('resource/sounds', 'shooting.wav'))
# FONT 
# GAME_OVER_FONT  = pygame.font.SysFont('comicsans', 40)             
# TEXTS
#gameOver_text    = GAME_OVER_FONT.render('Game over',1, YELLOW)      
# EVENTS 
# EXIT_GAME   = pygame.USEREVENT + 1


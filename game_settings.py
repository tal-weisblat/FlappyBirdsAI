

import pygame 
import numpy as np
import os
import random 
import torch 
import torch.nn as nn 
import time 



# WINDOW 
WIN_WIDTH   = 800
WIN_HEIGHT  = 450
GAME_WIDTH  = 450                                              
GAME_HEIGHT = 450   
WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))                      
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
BIRD_VEL    = 4
BIRD_JUMP   = 30
BIRD_FALL   = 1.5
BIRDS_NUM   = 150

# PILLARS 
PILLAR_WIDTH  = 50
PILLAR_HEIGHT = 200 
PILLAR_GAP    = 230
PILLARS_DIST  = 300

# sound  
DUPLICATION_SOUND = pygame.mixer.Sound(os.path.join('resource/sound', 'duplicate_parent.wav'))

# fonts 
DASHBOARD_FONT    = pygame.font.SysFont('comicsans', 20)

# dashboard 
X_DASHBOARD      = GAME_WIDTH + PILLAR_WIDTH
Y_DASHBOARD      = 0 
WIDTH_DASHBOARD  = WIN_WIDTH - GAME_WIDTH
HEIGHT_DASHBOARD = GAME_HEIGHT 
GAP_DASHBOARD    = 15

# generation number 
def generation_number_text(generation_number):
    return DASHBOARD_FONT.render('Generation: ' +str(generation_number) ,1, BLACK)
x_generation = X_DASHBOARD + GAP_DASHBOARD
y_generation = 1*GAP_DASHBOARD

# birds left  
def birds_number_text(birds_left):
    return DASHBOARD_FONT.render('Birds left: ' + str(birds_left) + ' / ' + str(BIRDS_NUM),1, BLACK)
x_birds_number = X_DASHBOARD + GAP_DASHBOARD
y_birds_number = 3*GAP_DASHBOARD

# generation time 
def generation_time_text(time):
    return DASHBOARD_FONT.render('Time: ' +str(time) ,1, BLACK)
x_time = X_DASHBOARD + GAP_DASHBOARD
y_time = 5*GAP_DASHBOARD

def game_time_text(game_time): 
    return DASHBOARD_FONT.render('Total time: ' +str(game_time) ,1, BLACK)
x_game_time = X_DASHBOARD + GAP_DASHBOARD
y_game_time = 7*GAP_DASHBOARD




# EVENTS 
# EXIT_GAME   = pygame.USEREVENT + 1


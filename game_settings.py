

import pygame 
import numpy as np
import os
import random 
import torch 
import torch.nn as nn 
import time 



# -------------- CONVERGENCE --------------
BIRDS_NUM   = 150      # birds 
BIRD_VEL    = 4
BIRD_FALL_VEL   = 3
BIRD_JUMP_VEL   = 40
PILLAR_GAP   = 230     # pillars  
PILLARS_DIST = 200
STD = 0.1              # controll mutation distribution 
# ------------------------------------------


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
BROWN   = (165,42,42)

# BIRDS 
BIRD_WIDTH  = 20
BIRD_HEIGHT = 20

# PILLARS 
PILLAR_WIDTH  = 50
PILLAR_HEIGHT = 200 


# sound  
DUPLICATION_SOUND = pygame.mixer.Sound(os.path.join('resource/sound', 'duplicate_parent.wav'))

# fonts 
DASHBOARD_FONT    = pygame.font.SysFont('comicsans', 20)


# DASHBOARD  
X_DASHBOARD      = GAME_WIDTH + PILLAR_WIDTH
Y_DASHBOARD      = 0 
WIDTH_DASHBOARD  = WIN_WIDTH - GAME_WIDTH
HEIGHT_DASHBOARD = GAME_HEIGHT 
GAP_DASHBOARD    = 15

# GENERATION NUMBER 
def generation_number_text(generation_number): return DASHBOARD_FONT.render('Generation: ' +str(generation_number) ,1, BLACK)
def birds_number_text(birds_left): return DASHBOARD_FONT.render('Birds left: ' + str(birds_left) + ' / ' + str(BIRDS_NUM),1, BLACK)
def generation_time_text(time):    return DASHBOARD_FONT.render('Time: ' +str(time) ,1, BLACK)
def game_time_text(game_time):     return DASHBOARD_FONT.render('Total time: ' +str(game_time) ,1, BLACK)

# CONVERGENCE FEATURES 
number_of_birds_text = DASHBOARD_FONT.render('Birds number: ' + str(BIRDS_NUM) ,1, BROWN)
birds_velocity_text = DASHBOARD_FONT.render('Birds velocity: ' + str(BIRD_VEL) ,1, BROWN)
birds_jump_velocity_text = DASHBOARD_FONT.render('Jump velocity: ' + str(BIRD_JUMP_VEL) ,1, BROWN)
birds_fall_velocity_text = DASHBOARD_FONT.render('Fall velocity: ' + str(BIRD_FALL_VEL) ,1, BROWN)
pillars_gap_text = DASHBOARD_FONT.render('Pillars gap: ' + str(PILLAR_GAP) ,1, BROWN)
pillars_distance_text = DASHBOARD_FONT.render('Pillars distance: ' + str(PILLARS_DIST) ,1, BROWN)
mutate_std_text = DASHBOARD_FONT.render('Mutation STD: ' + str(STD) ,1, BROWN)




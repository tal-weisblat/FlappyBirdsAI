

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
BLACK = (0,0,0)  
GREY  = (105,105,105)
PINK  = (255,192,203)  
WHITE = (255,255,255)
BROWN = (165,42,42)

# BIRDS 
BIRD_WIDTH  = 20
BIRD_HEIGHT = 20

# PILLARS 
PILLAR_WIDTH  = 50
PILLAR_HEIGHT = 200 


# sound  
DUPLICATION_SOUND = pygame.mixer.Sound(os.path.join('resource/sound', 'duplicate_parent.wav'))

# fonts 
DASHBOARD_TEXT_FONT    = pygame.font.SysFont('comicsans', 15)
DASHBOARD_TITLE_FONT    = pygame.font.SysFont('comicsans', 17)



# DASHBOARD  
X_DASHBOARD      = GAME_WIDTH + PILLAR_WIDTH
Y_DASHBOARD      = 0 
WIDTH_DASHBOARD  = WIN_WIDTH - (GAME_WIDTH + PILLAR_WIDTH)
HEIGHT_DASHBOARD = GAME_HEIGHT 
GAP_DASHBOARD    = 12

# STATUS
status_text = DASHBOARD_TITLE_FONT.render('Status', 1, BLACK)
def generation_number_text(generation_number): return DASHBOARD_TEXT_FONT.render('Generation: ' +str(generation_number) ,1, GREY)
def birds_number_text(birds_left): return DASHBOARD_TEXT_FONT.render('Birds left: ' + str(birds_left) + ' / ' + str(BIRDS_NUM),1, GREY)
def generation_time_text(time):    return DASHBOARD_TEXT_FONT.render('Time: ' +str(time) ,1, GREY)
def game_time_text(game_time):     return DASHBOARD_TEXT_FONT.render('Total time: ' +str(game_time) ,1, GREY)

# PARAMETERS (of convergence)  
parameters_text = DASHBOARD_TITLE_FONT.render('Parameters', 1, BLACK)
number_of_birds_text = DASHBOARD_TEXT_FONT.render('Birds number: ' + str(BIRDS_NUM) ,1, BROWN)
birds_velocity_text = DASHBOARD_TEXT_FONT.render('Birds velocity: ' + str(BIRD_VEL) ,1, BROWN)
birds_jump_velocity_text = DASHBOARD_TEXT_FONT.render('Jump velocity: ' + str(BIRD_JUMP_VEL) ,1, BROWN)
birds_fall_velocity_text = DASHBOARD_TEXT_FONT.render('Fall velocity: ' + str(BIRD_FALL_VEL) ,1, BROWN)
pillars_gap_text = DASHBOARD_TEXT_FONT.render('Pillars gap: ' + str(PILLAR_GAP) ,1, BROWN)
pillars_distance_text = DASHBOARD_TEXT_FONT.render('Pillars distance: ' + str(PILLARS_DIST) ,1, BROWN)
mutate_std_text = DASHBOARD_TEXT_FONT.render('Mutation STD: ' + str(STD) ,1, BROWN)

# SCORE 
scores_text = DASHBOARD_TITLE_FONT.render('Scores', 1, BLACK)



from game_settings import * 


# -------------------------------------- DRAW GAME -----------------------------------------
def draw_game(bird_list, pillar_list, generation_number, birds_left, generation_time, game_time, setup_score):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, PINK, (X_DASHBOARD, Y_DASHBOARD, WIDTH_DASHBOARD, HEIGHT_DASHBOARD))

    # status
    WIN.blit(status_text,    (X_DASHBOARD + WIDTH_DASHBOARD/2 - status_text.get_width()/2, 1*GAP_DASHBOARD))
    WIN.blit(generation_number_text(generation_number), (X_DASHBOARD + GAP_DASHBOARD, 3*GAP_DASHBOARD))
    WIN.blit(birds_number_text(birds_left),             (X_DASHBOARD + GAP_DASHBOARD, 5*GAP_DASHBOARD))
    WIN.blit(generation_time_text(generation_time),     (X_DASHBOARD + GAP_DASHBOARD, 7*GAP_DASHBOARD))
    WIN.blit(game_time_text(game_time),                 (X_DASHBOARD + GAP_DASHBOARD, 9*GAP_DASHBOARD))
    # parameters 
    WIN.blit(parameters_text,    (X_DASHBOARD + WIDTH_DASHBOARD/2 - parameters_text.get_width()/2, 12*GAP_DASHBOARD))
    WIN.blit(number_of_birds_text,                      (X_DASHBOARD + GAP_DASHBOARD, 14*GAP_DASHBOARD))
    WIN.blit(birds_velocity_text,                       (X_DASHBOARD + GAP_DASHBOARD, 16*GAP_DASHBOARD))
    WIN.blit(birds_jump_velocity_text,                  (X_DASHBOARD + GAP_DASHBOARD, 18*GAP_DASHBOARD))
    WIN.blit(birds_fall_velocity_text,                  (X_DASHBOARD + GAP_DASHBOARD, 20*GAP_DASHBOARD))
    WIN.blit(pillars_gap_text,                          (X_DASHBOARD + GAP_DASHBOARD, 22*GAP_DASHBOARD))
    WIN.blit(pillars_distance_text,                     (X_DASHBOARD + GAP_DASHBOARD, 24*GAP_DASHBOARD))
    WIN.blit(mutate_std_text,                           (X_DASHBOARD + GAP_DASHBOARD, 26*GAP_DASHBOARD))
    # scores 
    WIN.blit(scores_text,    (X_DASHBOARD + WIDTH_DASHBOARD/2 - scores_text.get_width()/2, 29*GAP_DASHBOARD))
    WIN.blit(setup_score_text(setup_score[-10:]), (X_DASHBOARD + GAP_DASHBOARD, 31*GAP_DASHBOARD))


    
    bird_list.draw()
    pillar_list.draw()
    pygame.display.update()

from game_settings import * 


# -------------------------------------- DRAW GAME -----------------------------------------
def draw_game(bird_list, pillar_list, generation_number, birds_left, generation_time, game_time):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, PINK, (X_DASHBOARD, Y_DASHBOARD, WIDTH_DASHBOARD, HEIGHT_DASHBOARD))

    WIN.blit(generation_number_text(generation_number), (X_DASHBOARD + GAP_DASHBOARD, 1*GAP_DASHBOARD))
    WIN.blit(birds_number_text(birds_left),             (X_DASHBOARD + GAP_DASHBOARD, 3*GAP_DASHBOARD))
    WIN.blit(generation_time_text(generation_time),     (X_DASHBOARD + GAP_DASHBOARD, 5*GAP_DASHBOARD))
    WIN.blit(game_time_text(game_time),                 (X_DASHBOARD + GAP_DASHBOARD, 7*GAP_DASHBOARD))

    WIN.blit(number_of_birds_text,                      (X_DASHBOARD + GAP_DASHBOARD, 9*GAP_DASHBOARD))
    WIN.blit(birds_velocity_text,                       (X_DASHBOARD + GAP_DASHBOARD, 11*GAP_DASHBOARD))
    WIN.blit(birds_jump_velocity_text,                  (X_DASHBOARD + GAP_DASHBOARD, 13*GAP_DASHBOARD))
    WIN.blit(birds_fall_velocity_text,                  (X_DASHBOARD + GAP_DASHBOARD, 15*GAP_DASHBOARD))
    WIN.blit(pillars_gap_text,                          (X_DASHBOARD + GAP_DASHBOARD, 17*GAP_DASHBOARD))
    WIN.blit(pillars_distance_text,                     (X_DASHBOARD + GAP_DASHBOARD, 19*GAP_DASHBOARD))
    WIN.blit(mutate_std_text,                           (X_DASHBOARD + GAP_DASHBOARD, 21*GAP_DASHBOARD))
    
    
    

    bird_list.draw()
    pillar_list.draw()
    pygame.display.update()
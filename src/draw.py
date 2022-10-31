
from game_settings import * 


# -------------------------------------- DRAW GAME -----------------------------------------
def draw_game(bird_list, pillar_list, generation_number, birds_left, generation_time, game_time):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, PINK, (X_DASHBOARD, Y_DASHBOARD, WIDTH_DASHBOARD, HEIGHT_DASHBOARD))

    WIN.blit(generation_number_text(generation_number), (x_generation, y_generation))
    WIN.blit(generation_time_text(generation_time), (x_time, y_time))
    WIN.blit(birds_number_text(birds_left), (x_birds_number, y_birds_number))
    WIN.blit(game_time_text(game_time), (x_game_time, y_game_time))
    
    
    
    
    
    bird_list.draw()
    pillar_list.draw()
    pygame.display.update()
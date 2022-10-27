
from game_settings import * 


# -------------------------------------- DRAW GAME -----------------------------------------
def draw_game(bird_list, pillar_list):
    WIN.fill(WHITE)
    bird_list.draw()
    pillar_list.draw()
    pygame.display.update()
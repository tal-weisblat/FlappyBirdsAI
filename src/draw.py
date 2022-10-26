
from game_settings import * 




def draw_game(bird_list, pillar_list):
    WIN.fill(WHITE)
    for bird in bird_list:
        bird.draw()
    pillar_list.draw()
    pygame.display.update()
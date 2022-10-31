
from operator import ge
from game_settings import * 
from src.objects import CreateBirdList, PillarList
from src.mutate  import mutateBird
from src.draw    import draw_game


    

def flappy_birds():

    start = time.time()
    generation_number = 1 
    birds_left = BIRDS_NUM
    bird_list = CreateBirdList()
    pillar_list = PillarList()
    pillar_list.add_pillar()
    clock = pygame.time.Clock() 
    run = True 

    while run:

        clock.tick(60) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False 

        # bird jump  
        bird_list.bird_jump(pillar_list)

        # move
        bird_list.bird_move()
        pillar_list.handle_pillars()

        # collisions 
        birds_left = bird_list.bird_hit_pillar(birds_left, pillar_list)
        birds_left = bird_list.bird_hit_walls(birds_left)

        # draw 
        draw_game(bird_list, pillar_list, generation_number, birds_left, round(time.time()-start,1))

        # duplication  
        if birds_left == 1:
            start = time.time()
            generation_number += 1 
            birds_left = 1 + BIRDS_NUM
            mutateBird(bird_list, BIRDS_NUM)     

flappy_birds()


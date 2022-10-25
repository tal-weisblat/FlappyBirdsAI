

from game_settings import * 
from objects import CreateBird, PillarList







def flappy_birds():

    bird        = CreateBird()
    pillar_list = PillarList()
    pillar_list.add_pillar()
    spacebar_pressed = False 
    clock = pygame.time.Clock() 
    run = True 

    while run:

        clock.tick(60) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False 

        # jump 
        keys = pygame.key.get_pressed()        
        spacebar_pressed = bird.jump(keys, spacebar_pressed)
        if keys[pygame.K_SPACE] == False: spacebar_pressed = False 

        # move
        bird.hover()
        pillar_list.move()

        # handle pillars 
        pillar_list.handle_pillars()

        # collisions 
        pillar_list.collision(bird)
        bird.bird_hit_frame()

        # draw 
        WIN.fill(WHITE)
        bird.draw()
        pillar_list.draw()
        pygame.display.update()
        
flappy_birds()
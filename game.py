# export KMP_DUPLICATE_LIB_OK=TRUE

from game_settings import * 
from src.objects import CreateBird, PillarList
from src.draw import draw_game


class Net(nn.Module):
    def __init__(self,input,H,output):
        super(Net,self).__init__()
        self.linear1=nn.Linear(input,H)
        self.linear2=nn.Linear(H,output)
    def forward(self,x):
        x=torch.sigmoid(self.linear1(x))  
        x=self.linear2(x)
        return x


def mutateBrain(brain):
        
    child = Net(4,4,1)

    # weights-1 (4X4 weights)
    for i in range(4):
        list_rand = np.random.normal(0,0.2,4) 
        list_rand = list_rand.tolist()
        child.linear1.weight.data[i] = brain.linear1.weight.data[i] + torch.tensor([list_rand])
    # weights-2 (4 weights)
    list_rand = np.random.normal(0,0.2,4) 
    list_rand = list_rand.tolist()
    child.linear2.weight.data = brain.linear2.weight.data + torch.tensor([list_rand])
    # bias-1 
    list_rand = np.random.normal(0,0.2,4)
    list_rand = list_rand.tolist()
    child.linear1.bias.data = brain.linear1.bias.data + torch.tensor([list_rand])
    # bias-2 
    list_rand = np.random.normal(0,0.2,1)
    list_rand = list_rand.tolist()
    child.linear2.bias.data = brain.linear2.bias.data + torch.tensor([list_rand])

    return child 





def flappy_birds():

    BIRDS_NUM = 100
    birds_left = BIRDS_NUM
    bird_list = [] 
    for i in range(BIRDS_NUM):
        bird = CreateBird()
        bird_list.append(bird)

    pillar_list = PillarList()
    pillar_list.add_pillar()
    #spacebar_pressed = False 
    clock = pygame.time.Clock() 
    run = True 

    while run:

        clock.tick(60) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False 

        # think 
        x,y = pillar_list.last_pillar_coordinates()
        x = float(x)
        y = float(y)
        for bird in bird_list:
            bird.think(x,y)

        # move
        for bird in bird_list:
            bird.hover()
        pillar_list.move()

        # handle pillars 
        pillar_list.handle_pillars()

        # collisions 
        for bird in bird_list:
            if pillar_list.collision(bird):
                birds_left = birds_left - 1 
                bird_list.remove(bird)
            elif bird.bird_hit_frame():
                birds_left = birds_left - 1 
                bird_list.remove(bird)

        # draw 
        draw_game(bird_list, pillar_list)
        

        print (birds_left)

        # STEP - duplications 
        if birds_left == 1:
            birds_left = 1 + BIRDS_NUM
            best_bird = bird_list[0]
            for i in range(BIRDS_NUM):
                child_brain = mutateBrain(best_bird.brain)
                bird = CreateBird()
                bird.brain = child_brain
                bird_list.append(bird)



flappy_birds()




# jump 
        # keys = pygame.key.get_pressed()        
        # spacebar_pressed = bird.jump(keys, spacebar_pressed)
        # if keys[pygame.K_SPACE] == False: spacebar_pressed = False 

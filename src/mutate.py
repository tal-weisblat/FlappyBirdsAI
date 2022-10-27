
from game_settings import * 
from src.objects import CreateBird, Net


def mutateBird(bird_list, BIRDS_NUM):

    # best-bird net 
    parent_bird = bird_list.list[0]
    parent_net = parent_bird.net

    # duplication 
    DUPLICATION_SOUND.play()
    for i in range(BIRDS_NUM):
       
        child_net = Net(4,4,1)
        # weights-1 (4X4 weights)
        for i in range(4):
            list_rand = np.random.normal(0,0.2,4) 
            list_rand = list_rand.tolist()
            child_net.linear1.weight.data[i] = parent_net.linear1.weight.data[i] + torch.tensor([list_rand])
        # weights-2 (4 weights)
        list_rand = np.random.normal(0,0.2,4) 
        list_rand = list_rand.tolist()
        child_net.linear2.weight.data = parent_net.linear2.weight.data + torch.tensor([list_rand])
        # bias-1 
        list_rand = np.random.normal(0,0.2,4)
        list_rand = list_rand.tolist()
        child_net.linear1.bias.data = parent_net.linear1.bias.data + torch.tensor([list_rand])
        # bias-2 
        list_rand = np.random.normal(0,0.2,1)
        list_rand = list_rand.tolist()
        child_net.linear2.bias.data = parent_net.linear2.bias.data + torch.tensor([list_rand])
        # add child to list 
        bird = CreateBird()
        bird.net = child_net
        bird_list.list.append(bird)
    


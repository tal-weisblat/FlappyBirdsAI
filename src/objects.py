
from game_settings import * 


# --------------------------------------------- NN -----------------------------------------------
class Net(nn.Module):
    def __init__(self,input,H,output):
        super(Net,self).__init__()
        self.linear1=nn.Linear(input,H)
        self.linear2=nn.Linear(H,output)
    def forward(self,x):
        x=torch.sigmoid(self.linear1(x))  
        x=self.linear2(x)
        return x


# -------------------------------------------- BIRD ---------------------------------------------
class CreateBird():
    def __init__(self):
        self.x = GAME_HEIGHT/5  
        self.y = GAME_HEIGHT/2
        self.width  = BIRD_WIDTH
        self.height = BIRD_HEIGHT
        self.rect = pygame.Rect (self.x, self.y, self.width, self.height)
        self.rect.topleft = (self.x,self.y)   
        self.net = Net(4,4,1)
        

# ----------------------------------------- BIRD-LIST -----------------------------------------
class CreateBirdList(CreateBird):

    def __init__(self):
        self.list = [] 
        for i in range(BIRDS_NUM):
            bird = CreateBird()
            self.list.append(bird)
            
    def add_bird(self):
        bird = CreateBird()
        self.list.append(bird)
        
    def draw(self):
        for bird in self.list: 
            pygame.draw.rect(WIN, BLACK, bird.rect)
    
    def remove_bird(self, bird):
        self.list.remove(bird)
    
    def bird_jump(self, pillar_list):   
        x,y = pillar_list.last_pillar_coordinates()
        x_pillar = float(x)
        y_pillar = float(y)
        for bird in self.list:     
            x_bird = float(bird.rect.x)   
            y_bird = float(bird.rect.y) 
            input = torch.tensor([[x_bird, y_bird, x_pillar, y_pillar]])
            output = bird.net.forward(input)    
            val = float(output[0][0])  
            val = (0.5*val) + 0.5        
            if val > 0.3: 
                bird.y = bird.y - BIRD_JUMP_VEL 
                bird.rect.topleft = (bird.x,bird.y)

    def bird_move(self):
        for bird in self.list:
            bird.y += BIRD_FALL_VEL 
            bird.rect.topleft = (bird.x,bird.y)

    def bird_hit_walls(self, birds_left):
        for bird in self.list: 
            if bird.rect.y <= 0: # ceiling 
                birds_left -= 1 
                self.list.remove(bird) 
            if bird.rect.y + BIRD_HEIGHT >= GAME_HEIGHT: # floor
                birds_left -= 1 
                self.list.remove(bird) 
        return birds_left

    def bird_hit_pillar(self, birds_left, pillar_list):
        for bird in self.list: 
            for pillar in pillar_list.list:
                if pillar[0].colliderect(bird.rect) or pillar[1].colliderect(bird.rect):
                    birds_left -= 1
                    self.list.remove(bird)

        return birds_left


# ---------------------------------------- PillarList ----------------------------------------
class PillarList():

    def __init__(self):
        self.list = [] 

    def add_pillar(self): 
        upper_pillar_height = random.randint(0, GAME_HEIGHT - PILLAR_GAP)     # create 
        lower_piller_height = GAME_HEIGHT - PILLAR_GAP - upper_pillar_height
        x = GAME_WIDTH
        y = GAME_HEIGHT - lower_piller_height
        lower_rect = pygame.Rect(x, y, PILLAR_WIDTH, lower_piller_height)  
        lower_rect.topleft = (x, y)
        upper_rect = pygame.Rect(x, 0, PILLAR_WIDTH, upper_pillar_height)    
        upper_rect.topleft = (x, 0)
        pillar = (lower_rect, upper_rect)  
        self.list.append(pillar)   # add
         
    def draw(self):
        for pillar in self.list:
            pygame.draw.rect(WIN, BLACK, pillar[0])
            pygame.draw.rect(WIN, BLACK, pillar[1])
            
    def collision(self, bird): 
        for pillar in self.list:
            if pillar[0].colliderect(bird.rect) or pillar[1].colliderect(bird.rect):
                return True 
        return False 
        
    def handle_pillars(self): 
        # move 
        for pillar in self.list:      
            pillar[0].x -= BIRD_VEL
            pillar[1].x -= BIRD_VEL
        # remove & add 
        first_pillar =  self.list[0] 
        last_pillar  =  self.list[-1]
        if first_pillar[0].x <= -PILLAR_WIDTH:
            self.list.remove(first_pillar)
        
        # if last_pillar[0].x <= PILLARS_DIST:   
        if GAME_WIDTH - (last_pillar[0].x + PILLAR_WIDTH) >= PILLARS_DIST:
            self.add_pillar()
        
    def last_pillar_coordinates(self):
        last_pillar = self.list[-1:][0]
        x = last_pillar[0].x
        y = last_pillar[0].y 
        return x,y




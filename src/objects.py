
from game_settings import * 


# -------------------------------------------- NN -----------------------------------------------
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
        self.brain = Net(4,4,1)
        
    def think(self, x_pillar, y_pillar):
        
        x_bird = float(self.rect.x)   
        y_bird = float(self.rect.y) 

        input = torch.tensor([[x_bird, y_bird, x_pillar, y_pillar]])
        output = self.brain.forward(input)
    
        
        val = float(output[0][0])  
        val = (0.5*val) + 0.5
        #print(val)
        
        if val > 0.3: 
            self.y = self.y - BIRD_JUMP 
            self.rect.topleft = (self.x,self.y)



    def draw(self):
        pygame.draw.rect(WIN, BLACK, self.rect)

    def jump(self, keys, spacebar_pressed): 
        if keys[pygame.K_SPACE] and (spacebar_pressed == False) : 
            self.y = self.y - BIRD_JUMP 
            self.rect.topleft = (self.x,self.y)
            spacebar_pressed = True 
            return spacebar_pressed

    def hover(self):
        self.y += BIRD_FALL 
        self.rect.topleft = (self.x,self.y)

    def bird_hit_frame(self):
        if self.rect.y <= 0:   # ceiling 
            return True 
        if self.rect.y + BIRD_HEIGHT >= GAME_HEIGHT:   # ground 
            return True 
        return False 




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
        self.list.append(pillar)                                                # add
         
    def draw(self):
        for pillar in self.list:
            pygame.draw.rect(WIN, BLACK, pillar[0])
            pygame.draw.rect(WIN, BLACK, pillar[1])

    def move(self):
        for pillar in self.list: 
            pillar[0].x -= BIRD_VEL
            pillar[1].x -= BIRD_VEL
            
    def collision(self, bird): 
        for pillar in self.list:
            if pillar[0].colliderect(bird.rect) or pillar[1].colliderect(bird.rect):
                return True 
        return False 
        

    def handle_pillars(self): 
        last_pillar = self.list[-1:][0]
        if last_pillar[0].x <= PILLARS_DIST:
            self.add_pillar()
        if last_pillar[0].x <= 50:
            self.list.remove(last_pillar)

    def last_pillar_coordinates(self):
        last_pillar = self.list[-1:][0]
        x = last_pillar[0].x
        y = last_pillar[0].y 
        return x,y




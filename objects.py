
from game_settings import * 




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
                print ('collision')
         
    def handle_pillars(self): 
        last_pillar = self.list[-1:][0]
        if last_pillar[0].x <= PILLARS_DIST:
            self.add_pillar()
        if last_pillar[0].x <= 50:
            self.list.remove(last_pillar)



# -------------------------------------------- BIRD ---------------------------------------------
class CreateBird():

    def __init__(self):
        self.x = GAME_HEIGHT/5  
        self.y = GAME_HEIGHT/2
        self.width  = BIRD_WIDTH
        self.height = BIRD_HEIGHT
        self.rect = pygame.Rect (self.x, self.y, self.width, self.height)
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
        if self.rect.y <= 0:
            print ('bird hit ceiling')
        if self.rect.y + BIRD_HEIGHT >= GAME_HEIGHT:
            print ('bird hit the ground')
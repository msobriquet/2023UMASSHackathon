import pygame
import sys
from random import randrange

class Dot(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        super().__init__()
        self.image = pygame.image.load('graphics/dot.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height)) #whatever size in here is the size of the rect
        self.rect = self.image.get_rect() #just draws a rect directly around it
        self.rect.center = [x, y]

    def update(self):
        self.rect.move_ip(-8, 0)
        
class Girl(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y) -> None: #if i need width and height attributes I can add them
        super().__init__()
        self.image = pygame.image.load('graphics/girl.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height)) 
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 8
        self.isLeft = False
        self.isRight = False
        self.jumpCount = 10
        self.isJump = False

    def update(self): 
        if self.isLeft == True:
            self.rect.centerx -= self.vel
            self.isLeft = False

        if self.isRight == True:
            self.rect.centerx += self.vel
            self.isRight = False

        if self.isJump == True:
            if self.jumpCount >= -10:
                self.rect.centery -= (self.jumpCount * abs(self.jumpCount)) * 0.4
                self.jumpCount -= 0.4
            else:
                self.rect.centery = 530
                self.jumpCount = 10
                self.isJump = False    

class Background:
    def __init__(self, x):
        self.width = WIDTH
        self.height = HEIGHT
        self.x = x
        self.y = 0
        self.set_texture()
        self.show()

    def update(self, dx):
        self.x += dx 
        if self.x <= -WIDTH:
            self.x = WIDTH     

    def show(self):
        screen.blit(self.texture, (self.x, self.y))

    def set_texture(self):
        self.texture = pygame.image.load('graphics/bg3.png').convert()
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

class Game:
    def __init__(self) -> None:
        self.background = [Background(0), Background(WIDTH)]
        self.speed = 3
        self.girl = Girl(150, 380, 275, 530)
        self.girlGroup = pygame.sprite.Group()
        self.dotGroup = pygame.sprite.Group()
        self.girlGroup.add(self.girl)
        self.damageScore = 0 # num of collisions with dots
        self.scoreFont = pygame.font.SysFont('Menlo', 30)
        self.titleFont = pygame.font.SysFont('Menlo', 150, bold = True)

#general setup
pygame.init()
clock = pygame.time.Clock()

#game screen
WIDTH = 1280
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#song data
#where the beats of the song hit in seconds
data = [] 
for i in range(30): #will be multiplied by 2 so 60 secs
    seed = (randrange(0, 200))/100 #random float between 0-2
    data.append(seed + (i * 1.5))   

#create game object
thisGame = Game()

#start screen loop
def start():
    running = True

    #music
    pygame.mixer.music.load('audio/file_example.wav')
    pygame.mixer.music.play(0)  
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False    
                sys.exit()

        screen.fill("darkolivegreen3")

        text_surface1 = thisGame.titleFont.render("Ritathm", True, (0, 0, 0))
        text_surface2 = thisGame.scoreFont.render("Press s to start!", True, (0,0,0))


        screen.blit(text_surface1, (320, 200))
        screen.blit(text_surface2, (400, 400))
        pygame.display.flip()
        clock.tick(60)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            s_time = pygame.time.get_ticks()/1000
            return s_time
        

#game loop
def main(start_time):
    running = True
    l_time = 0 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

    
        #background
        for bg in thisGame.background:
            bg.update(-thisGame.speed) #paralax effect
            bg.show()  #constructor only shows it once so we need to show it every time

        #score
        text_surface = thisGame.scoreFont.render("Score: " + str(len(data) - thisGame.damageScore)+ " out of " + str(len(data)), True, (0, 0, 0))    

        # See if the Sprite block has collided with anything in the Group dotGroup
        # The True flag will remove the sprite in block_list
        dot_group_hits = pygame.sprite.spritecollide(thisGame.girl, thisGame.dotGroup, True)

        # Check the list of colliding sprites, and add one to the score for each one
        for hit in dot_group_hits:
            thisGame.damageScore +=1    

        #player
        keys = pygame.key.get_pressed()

        if not thisGame.girl.isJump:
            if keys[pygame.K_SPACE]:
                thisGame.girl.isJump = True
        else:
            thisGame.girlGroup.update()

        if keys[pygame.K_LEFT] and thisGame.girl.rect.centerx > thisGame.girl.vel:  # Making sure the top left position of our character is greater than our vel so we never move off the screen.
            thisGame.girl.isLeft = True
            thisGame.girlGroup.update()

        if keys[pygame.K_RIGHT] and thisGame.girl.rect.centerx <  WIDTH:  # Making sure the top right corner of our character is less than the screen width
            thisGame.girl.isRight = True
            thisGame.girlGroup.update()   

        #dots
        thisGame.dotGroup.update()

        c_time = (pygame.time.get_ticks()/1000) - start_time

        for i in range(len(data)):
            if c_time >= data[i] and l_time < data[i]:
                dot = Dot(80, 80, 1280, 590)
                thisGame.dotGroup.add(dot)

        l_time = c_time

        #rendering
        thisGame.dotGroup.draw(screen)
        thisGame.girlGroup.draw(screen)

        screen.blit(text_surface, (5,5))

        if c_time > (data[-1] + 5) :
            #screen.fill("black") not doing anything anyway
            pygame.time.set_timer(sys.exit(), 100000)

        pygame.display.update()
        clock.tick(60)    

start_time = start()                
main(start_time)



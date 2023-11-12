import pygame

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
        self.isJump = False
        self.jumpCount = 20

    def update(self): 
        if self.isLeft == True:
            self.rect.centerx -= self.vel
            self.isLeft = False

        if self.isRight == True:
            self.rect.centerx += self.vel
            self.isRight = False

        if self.isJump == True:
            if self.jumpCount >= -20:
                self.rect.move_ip(0, -(self.jumpCount * abs(self.jumpCount)) * 0.3) #auto updates rect object
                self.jumpCount -= 1
            else:
                self.rect.move_ip(0, 0)
                self.jumpCount = 20
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
        self.girl = Girl(150, 380, 275, 550)
        self.girl_group = pygame.sprite.Group()
        self.dot_group = pygame.sprite.Group()
        self.girl_group.add(self.girl)
        self.damage_score = 0 # num of collisions with dots
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

#general setup
pygame.init()
clock = pygame.time.Clock()

#game screen
WIDTH = 1280
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#song data
data = [5.000, 7.000, 9.000, 11.000] #where the beats of the song hit in seconds

#game loop
def main():
    running = True
    thisGame = Game()
    l_time = 0


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #background
        for bg in thisGame.background:
            bg.update(-thisGame.speed) #paralax effect
            bg.show()  #constructor only shows it once so we need to show it every time

        #score
        text_surface = thisGame.font.render("Score:" + str(len(data) - thisGame.damage_score)+ " out of " + str(len(data)), False, (0, 0, 0))    

        # See if the Sprite block has collided with anything in the Group dot_group
        # The True flag will remove the sprite in block_list
        dot_group_hits = pygame.sprite.spritecollide(thisGame.girl, thisGame.dot_group, True)

        # Check the list of colliding sprites, and add one to the score for each one
        for hit in dot_group_hits:
            thisGame.damage_score +=1    

        #player
        keys = pygame.key.get_pressed()

        if not thisGame.girl.isJump:
            if keys[pygame.K_SPACE]:
                thisGame.girl.isJump = True
        else:
            thisGame.girl_group.update()

        if keys[pygame.K_LEFT] and thisGame.girl.rect.centerx > thisGame.girl.vel:  # Making sure the top left position of our character is greater than our vel so we never move off the screen.
            thisGame.girl.isLeft = True
            thisGame.girl_group.update()

        if keys[pygame.K_RIGHT] and thisGame.girl.rect.centerx <  WIDTH:  # Making sure the top right corner of our character is less than the screen width
            thisGame.girl.isRight = True
            thisGame.girl_group.update()   


        #dots
        thisGame.dot_group.update()

        print("current time:")
        c_time = pygame.time.get_ticks()/1000
        print(c_time)

        print("last time:")
        print(l_time)
        print("-----------")

        for i in range(len(data)):
            if c_time >= data[i] and l_time < data[i]:
                dot = Dot(80, 80, 1280, 600)
                thisGame.dot_group.add(dot)

        l_time = c_time

        #rendering
        thisGame.dot_group.draw(screen)
        thisGame.girl_group.draw(screen)

        screen.blit(text_surface, (0,0))

        pygame.display.update()
        clock.tick(60)
                
main()

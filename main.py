import pygame

class Dot(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        super().__init__()
        self.image = pygame.image.load('graphics/note.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height)) #whatever size in here is the size of the rect
        self.rect = self.image.get_rect() #just draws a rect directly around it
        self.rect.center = [x, y]

    def update(self):
        self.rect.move_ip(-5, 0)
        
class Girl(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y) -> None: #if i need width and height attributes I can add them
        super().__init__()
        self.image = pygame.image.load('graphics/mc.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height)) 
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.isJump = False
        self.jumpCount = 10

    def update(self): 
        if self.isJump == True:
            if self.jumpCount >= -10:
                self.rect.move_ip(0, -(self.jumpCount * abs(self.jumpCount)) * 0.5) #auto updates rect object
                self.jumpCount -= 1
            else:
                self.rect.move_ip(0, 0)
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
        self.girl = Girl(300, 300, 275, 550)
        self.girl_group = pygame.sprite.Group()
        self.dot_group = pygame.sprite.Group()
        self.girl_group.add(self.girl)

#general setup
pygame.init()
clock = pygame.time.Clock()

#game screen
WIDTH = 1280
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#song data
data = [5.000, 6.000, 7.000, 8.000] #where the beats of the song hit in seconds

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

        #player
        keys = pygame.key.get_pressed()

        if not thisGame.girl.isJump:
            if keys[pygame.K_SPACE]:
                thisGame.girl.isJump = True
        else:
            thisGame.girl_group.update()


        thisGame.dot_group.update()

        print("current time:")
        c_time = pygame.time.get_ticks()/1000
        print(c_time)

        print("last time:")
        print(l_time)
        print("-----------")

        for i in range(len(data)):
            if c_time >= data[i] and l_time < data[i]:
                dot = Dot(100, 100, 1280, 400)
                thisGame.dot_group.add(dot)

        l_time = c_time

        thisGame.dot_group.draw(screen)
        thisGame.girl_group.draw(screen)

        pygame.display.update()
        clock.tick(60)
                
main()

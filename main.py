import pygame

class Dot(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('graphics/note.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height)) #whatever size in here is the size of the rect
        self.rect = self.image.get_rect() #just draws a rect directly around it
        self.rect.center = [pos_x, pos_y]

    def update(self):
        self.rect.move_ip(-5, 0)
        
class Girl:
    def __init__(self, x, y) -> None:
        self.width = 300
        self.height = 300
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 10
        self.set_texture()
        self.show()

    def update(self, dx):
        self.x += dx

    def show(self):
        screen.blit(self.texture, (self.x, self.y))
        # self.rect = self.texture.get_rect(center = (self.x, self.y))
        # screen.blit(self.texture, self.rect)

    def set_texture(self):
        self.texture = pygame.image.load('graphics/mc.png').convert_alpha()
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))
        #mc_rect = self.get_rect(center = (275, 550))

    def jump(self):
        if self.jumpCount >= -10:
            print(self.jumpCount)
            self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
            self.jumpCount -= 1
        else:
            self.y = 400
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
        self.girl = Girl(275,550)
        self.dot_group = pygame.sprite.Group()

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
        thisGame.girl.show()

        keys = pygame.key.get_pressed()

        if not thisGame.girl.isJump:
            if keys[pygame.K_SPACE]:
                thisGame.girl.isJump = True
        else:
            thisGame.girl.jump()

        thisGame.girl.update(0)

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

        pygame.display.update()
        clock.tick(60)
                
main()

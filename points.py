import pygame
screen = pygame.display.set_mode()
class Points(pygame.sprite.Sprite):

    def __init__(self,x,y):
        self.width = 30
        self.height = 20
        self.x = x #x coordinate #move points -> move x coordinator
        self.y= y #y values unchanged
        self.set_texture()
        self.show()

    #     super(Points, self).__init__()
    #     img = pygame.image.load("graphics/note.png")
    #     img =  pygame.transform.scale(img, (int(img.get_size)*0.65, int(img.get_size)*0.65))

    def update(self, dx):
        self.x += dx #dx 

    def show(self):
        screen.blit(self.texture, (self.x, self.y))

    def set_texture(self):
        path = os.path.join("graphics/note.png")
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

    
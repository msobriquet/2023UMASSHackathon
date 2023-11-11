class Points():
    def __init__(self,x,y):
        self.width = 10
        self.height = 20
        self.x = x
        self.y = y
        self.set_texture()
        self.show()
    def update(self, dx):
        self.x += dx

    def show(self):
        screen.blit(self.texture, (self.x, self.y))

    def set_texture(self):
        path = os.path.join("graphics/note.png")
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 800))
clock = pygame.time.Clock()

bg_surf = pygame.image.load('graphics/background.png').convert()
bg_surf = pygame.transform.scale(bg_surf, (1280, 800))

mc_surf = pygame.image.load('graphics/mc.png').convert()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    screen.blit(bg_surf ,(0,0))


    pygame.display.flip()

    clock.tick(60)
                



import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 800))
clock = pygame.time.Clock()

bg_surf = pygame.image.load('graphics/background.png').convert()
bg_surf = pygame.transform.scale(bg_surf, (1280, 800))

mc_surf = pygame.image.load('graphics/mc.png').convert_alpha()
mc_surf = pygame.transform.scale(mc_surf, (300,300))
mc_rect = mc_surf.get_rect(center = (275, 550))

running = True
mc_gravity = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    screen.blit(bg_surf ,(0,0))

    #player
    mc_gravity += 1  
    mc_rect.y += mc_gravity  
    screen.blit(mc_surf, mc_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
       if mc_rect.y > 
        
    

    pygame.display.flip()
    clock.tick(60)
                


#make player jump
#make moving dot 
#collision detection

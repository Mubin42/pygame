import pygame

# initializing pygame

pygame.init()

# display.set_mode takes an tuple and sets it to the regulation
display = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Screen")
FPS = 60
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

import pygame

pygame.init()

display = pygame.display.set_mode((350, 720))
clock = pygame.time.Clock()
fps = 60
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()

pygame.quit()

import pygame
import sys
from game import Game


pygame.init()

# colors
dark_blue = (44, 44, 127)


# display surface
screen_width, screen_height, fps = 300, 600, 60
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tetris')

clock = pygame.time.Clock()
game = Game()

# event loop
while True:
    for event in pygame.event.get():
        # close the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # move block
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_SPACE:
                game.rotate()

    # Draw colors
    screen.fill(dark_blue)
    game.draw(screen)
    pygame.display.update()
    clock.tick(fps)

import pygame
import sys

from grid import Grid
from blocks import *

pygame.init()

# colors
dark_blue = (44, 44, 127)

game_grid = Grid()

block = ZBlock()

# display surface
screen_width, screen_height, fps = 300, 600, 60
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tetris')

clock = pygame.time.Clock()

# event loop
while True:
    for event in pygame.event.get():
        # close the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Draw colors
    screen.fill(dark_blue)
    game_grid.draw(screen)

    block.draw(screen)
    pygame.display.update()
    clock.tick(fps)

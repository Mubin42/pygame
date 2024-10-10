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

# custom event
GAME_UPDATE = pygame.USEREVENT
# update every 0.2 seconds (200 milliseconds)
pygame.time.set_timer(GAME_UPDATE, 200)

# event loop
while True:
    for event in pygame.event.get():
        # close the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # update every 0.2 seconds
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()
        # move block
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.game_over = False
                game.reset()

            if event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()
            if event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()
            if event.key == pygame.K_DOWN and not game.game_over:
                game.move_down()
            if event.key == pygame.K_SPACE and not game.game_over:
                game.rotate()

    # Draw colors
    screen.fill(dark_blue)
    game.draw(screen)

    pygame.display.update()
    clock.tick(fps)

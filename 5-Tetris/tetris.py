import pygame
import sys
from game import Game
from colors import Colors

pygame.init()

# create font
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("Game Over", True, Colors.white)


score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

# display surface
screen_width, screen_height, fps = 500, 620, 60
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
                game.update_score(0, 1)
            if event.key == pygame.K_SPACE and not game.game_over:
                game.rotate()

    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    # Draw colors
    screen.fill(Colors.dark_blue)

    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))
    # only display game over if the game is over
    if game.game_over:
        screen.blit(game_over_surface, (320, 450, 50, 50))
    pygame.draw.rect(screen, Colors.light_blue, score_rect)
    # draw score
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect)
    game.draw(screen)

    pygame.display.update()
    clock.tick(fps)

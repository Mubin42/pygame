"""
Tutorial: https://www.youtube.com/watch?v=1_H7InPMjaY
Material: Completed
"""

import pygame


def bouncing_rect():
    global rectangle_one_x_speed, rectangle_one_y_speed, rectangle_two_x_speed, rectangle_two_y_speed

    rectangle_one.x += rectangle_one_x_speed
    rectangle_one.y += rectangle_one_y_speed

    # collision with screen borders
    if rectangle_one.right >= screen_width or rectangle_one.left <= 0:
        rectangle_one_x_speed *= -1

    if rectangle_one.bottom >= screen_height or rectangle_one.top <= 0:
        rectangle_one_y_speed *= -1

    # drawing the rectangle
    pygame.draw.rect(display, rectangle_one_color, rectangle_one)
    pygame.draw.rect(display, rectangle_two_color, rectangle_two)


# initializing pygame
pygame.init()

# defining variables
screen_width, screen_height = 600, 600
fps = 60
running = True

# creating display and clocks
display = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption(title="Collision Physics")

# dimension x, dimension y, pixels y, pixels x
rectangle_one = pygame.Rect(100, 100, 50, 50)  # dimension x, dimension y, pixel x, pixel y
rectangle_one_color = (255, 255, 255)
rectangle_one_x_speed, rectangle_one_y_speed = 5, 4

rectangle_two = pygame.Rect(100, 100, 50, 50)  # dimension x, dimension y, pixel x, pixel y
rectangle_two_color = (30, 150, 150)
rectangle_two_x_speed, rectangle_two_y_speed = 6, 5


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.fill((30, 30, 30))  # rgb(red, green, blue) [0 - 255]
    bouncing_rect()
    pygame.display.update()
    clock.tick(fps)

pygame.quit()

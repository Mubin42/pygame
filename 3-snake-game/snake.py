import pygame
import random


# function to handle the score
def print_score(score):
    text = score_font.render(f"Score: {score}", True, orange)
    display.blit(text, [0, 0])


# key movement of snake
def key_movement():
    global x_speed, y_speed
    # if key is press -> this is true
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_speed = - unit_size
            y_speed = 0

        if event.key == pygame.K_RIGHT:
            x_speed = unit_size
            y_speed = 0

        if event.key == pygame.K_DOWN:
            y_speed = unit_size
            x_speed = 0

        if event.key == pygame.K_UP:
            y_speed = - unit_size
            x_speed = 0


# draw a snake
def draw_snake(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(display, white, [pixel[0], pixel[1], size, size])


# generate random coordinate for the food
def generate_coordinate():
    target_x = round(random.randrange(0, display_width - unit_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, display_height - unit_size) / 10.0) * 10.0

    return target_x, target_y


# initializing pygame
pygame.init()

# variables
isRunning = True
unit_size = 10
fps = 15

# colors
white = (255, 255, 255)
black = (15, 15, 15)
red = (255, 0, 0)
orange = (255, 165, 0)

# create display
display_width, display_height = 600, 400
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# initializing fonts
score_font = pygame.font.SysFont("ubuntu", 24)

# snake
x = display_width / 2  # initial position of snake x
y = display_height / 2  # initial position of snake y

x_speed = 0  # speed of snake in x-axis
y_speed = 0  # speed of snake in y-axis

snake_length = 1
snake_pixels = []

# food variables
food_x, food_y = generate_coordinate()

# event loop
while isRunning:
    for event in pygame.event.get():
        # exit game -> if this is true
        if event.type == pygame.QUIT:
            isRunning = False

        key_movement()

    if x >= display_width or x <= 0 or y >= display_height or y < 0:  # Check if the snake hits the boundaries
        isRunning = False

    # move the snake
    x += x_speed
    y += y_speed

    display.fill(black)

    # make the food for the first time
    pygame.draw.rect(display, orange, [food_x, food_y, unit_size, unit_size])

    # tracking the path
    snake_pixels.append([x, y])

    # making the snake tail
    if len(snake_pixels) > snake_length:
        del snake_pixels[0]

    for pixel in snake_pixels[: -1]:  # Iterate over each segment of the snake except the head
        if pixel == [x, y]:  # Check if the snake collides with itself
            isRunning = False

    draw_snake(unit_size, snake_pixels)
    print_score(snake_length)
    pygame.display.update()

    # if you eat the food, the size will increase, and food reappears
    if x == food_x and y == food_y:
        food_x, food_y = generate_coordinate()
        snake_length += 1

    clock.tick(fps)

# ending pygame
pygame.quit()
quit()

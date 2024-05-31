import pygame


# rectangle movement
def rect_movement():
    global x, y

    rect.x += x
    rect.y += y

    # do bouncing thing
    if rect.right >= display_width or rect.left <= 0:
        x *= -1

    if rect.bottom >= display_height or rect.top <= 0:
        y *= -1

    pygame.draw.rect(display, white, rect)


# initializing pygame
pygame.init()

# colors
black = (15, 15, 15)
white = (255, 255, 255)

# variables
display_width, display_height = 800, 600
fps = 30
running = True

# create display
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Moving Rectangle")
clock = pygame.time.Clock()

# codes for rectangle
x, y = 5, 4
rect = pygame.Rect(100, 100, 50, 50)  # x position, y position, x size, y size


# event loop
while running:
    # closing login
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # rest of my codes
    display.fill(black)
    rect_movement()
    pygame.display.update()
    clock.tick(fps)

# ending pygame
pygame.quit()
quit()

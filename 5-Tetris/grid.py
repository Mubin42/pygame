import pygame
from colors import Colors


class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for col in range(self.num_cols)] for row in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                # X and Y position with 1px padding
                x = column * self.cell_size + 1
                y = row * self.cell_size + 1
                size = self.cell_size - 1
                # draw rect
                cell_rect = pygame.Rect(x, y, size, size)

                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

from grid import Grid
from blocks import *
import random


class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False

    def get_random_block(self):
        # cycle through the blocks, make sure each block appears once before repeating
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(-1, 0)
            self.lock_block()

    def rotate(self):
        self.current_block.rotate()
        if not self.block_inside():
            self.current_block.undo_rotate()

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()

        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False

        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)

    # lock the block in place in the bottom of the grid and get a new block
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()

        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id

        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        self.grid.clear_full_rows()

        if not self.block_fits():
            self.game_over = True

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()

        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.column):
                return False
        return True

    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

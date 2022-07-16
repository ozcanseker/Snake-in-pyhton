import copy

from src.game_logic.classes.Block import Block


class Snake:

    def __init__(self, length, init_pos_x, init_pos_y, width, height):
        self.length = length
        self.blocks = []
        self.board_width = width
        self.board_height = height

        for i in range(length):
            self.blocks.append(Block(init_pos_x + i, init_pos_y))

    def get_snake_pos(self):
        return copy.deepcopy(self.blocks)

    def grow_longer(self):
        self.blocks.append(copy.deepcopy(self.blocks[len(self.blocks) - 1]))

    def get_head_pos(self):
        return copy.deepcopy(self.blocks[0])

    def move_to_left(self):
        self._make_body_follow()

        self.blocks[0].setX(
            (self.blocks[0].x - 1 + self.board_width) % self.board_width
        )

    def move_to_top(self):
        self._make_body_follow()

        self.blocks[0].setY(
            (self.blocks[0].y - 1 + self.board_height) % self.board_height
        )

    def move_to_bot(self):
        self._make_body_follow()

        self.blocks[0].setY(
            (self.blocks[0].y + 1 + self.board_height) % self.board_height
        )

    def move_to_right(self):
        self._make_body_follow()

        self.blocks[0].setX(
            (self.blocks[0].x + 1 + self.board_width) % self.board_width
        )

    def _make_body_follow(self):
        for i in range(len(self.blocks) - 1, 0, -1):
            self.blocks[i].x = self.blocks[i-1].x
            self.blocks[i].y = self.blocks[i-1].y


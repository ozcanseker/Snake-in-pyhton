from random import randint
from src.game_logic.classes.Snake import Snake
from src.game_logic.classes.Block import Block
from src.variables.input import GameInput, MovementInput


class Gameboard:
    def __init__(self, width, height, snake_length):
        self.width = width
        self.height = height
        self.snake = Snake(snake_length, width // 2, height // 2, width, height)

        self._init_matrix()
        self._create_apple()

        self.game_running = True
        self.game_over = False
        self.input = MovementInput.LEFT

    def update(self):
        if self.game_running:
            if self.input == MovementInput.TOP:
                self.move_snake_top()
            elif self.input == MovementInput.BOTTOM:
                self.move_snake_bottom()
            elif self.input == MovementInput.RIGHT:
                self.move_snake_right()
            elif self.input == MovementInput.LEFT:
                self.move_snake_left()

        self.check_if_apple()

        self.check_if_biting_self()

    def check_if_apple(self):
        snakehead = self.snake.get_head_pos()

        if self.apple.check_same_pos(snakehead):
            self.snake.grow_longer()
            self._create_apple()

    def check_if_biting_self(self):
        snakehead = self.snake.get_head_pos()
        snake = self.snake.get_snake_pos()

        for i in range(1, len(snake)):
            if snakehead.check_same_pos(snake[i]):
                self.game_over = True
                self.game_running = False

    def set_input(self, user_input):
        if isinstance(user_input, MovementInput):
            if self.check_if_valid_move(user_input):
                self.input = user_input
        elif user_input == GameInput.QUIT:
            self.game_running = False

    def check_if_valid_move(self, user_input):
        return (user_input == MovementInput.RIGHT and self.input != MovementInput.LEFT) or \
                    (user_input == MovementInput.LEFT and self.input != MovementInput.RIGHT) or \
                    (user_input == MovementInput.TOP and self.input != MovementInput.BOTTOM) or \
                    (user_input == MovementInput.BOTTOM and self.input != MovementInput.TOP)

    def move_snake_left(self):
        self.snake.move_to_left()

    def move_snake_top(self):
        self.snake.move_to_top()

    def move_snake_bottom(self):
        self.snake.move_to_bot()

    def move_snake_right(self):
        self.snake.move_to_right()

    def _init_matrix(self):
        self.matrix = [self.height * [0]] * self.width

    def _create_apple(self):
        self.apple = Block(randint(0, self.height - 1), randint(0, self.width - 1))

    def get_snake_pos(self):
        return self.snake.get_snake_pos()

    def get_apple_pos(self):
        return self.apple.get_copy()

    def get_game_running(self):
        return self.game_running


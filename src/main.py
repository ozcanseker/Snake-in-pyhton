import pygame
import src.variables.colors as colors

from src.game_logic.Gameboard import Gameboard
from src.variables.input import GameInput, MovementInput

# Options
starting_snake_length = 5
squares = 50
square_line_width = 1
square_width = 15
window_size = (squares * square_width, squares*square_width)

def start_game():
    global gameboard
    global screen
    global clock
    global user_quit
    global font

    # init steps
    pygame.init()
    pygame.display.set_caption("Snake")

    screen = pygame.display.set_mode(window_size)
    clock = pygame.time.Clock()
    user_quit = False

    pygame.font.init()
    font = pygame.font.SysFont(None, 50)

    gameboard = None

    # call game
    main_loop()

    #close game
    close_game()


def main_loop():
    global gameboard

    while not user_quit:
        draw_continue_screen()
        check_if_player_continue()

        if gameboard is not None:
            game_play_loop()
            gameboard = None

def draw_continue_screen():
    screen.fill((0, 0, 0))
    text_surface = font.render("ESC to quit          Space to continue", True, colors.WHITE)
    screen.blit(text_surface, (0,0))

    pygame.display.flip()


def check_if_player_continue():
    global gameboard
    global user_quit

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            user_quit = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                user_quit = True
            elif event.key == pygame.K_SPACE:
                # init game object
                gameboard = Gameboard(squares, squares, starting_snake_length)


def game_play_loop():
    while gameboard.get_game_running():
        # Close the loop if the player exits the game
        get_player_input()

        gameboard.update()

        #draw board
        draw_main_board()

        clock.tick(15)


def draw_main_board():
    screen.fill((0, 0, 0))
    spacing_from_line = (square_line_width / 2)
    spacing_to_line = (square_width - spacing_from_line)

    for i in range(squares + 1):
        square_spacing = (i * square_width) - (square_line_width / 2)

        # vertical
        pygame.draw.rect(screen, colors.DARK_RED, pygame.Rect(square_spacing, 0, square_line_width, window_size[0]))
        # horizontal
        pygame.draw.rect(screen, colors.DARK_RED, pygame.Rect(0, square_spacing, window_size[0], square_line_width))


    # Draw apple
    apple_pos = gameboard.get_apple_pos()

    pygame.draw.rect(screen,
                     colors.GREEN,
                     pygame.Rect((apple_pos.x * square_width) + spacing_from_line,
                                 (apple_pos.y * square_width) + spacing_from_line,
                                 spacing_to_line,
                                 spacing_to_line)
                     )

    # draw the snake
    snake_pos = gameboard.get_snake_pos()

    for sp in snake_pos:
        pygame.draw.rect(screen,
                         colors.BlUE,
                         pygame.Rect((sp.x * square_width) + spacing_from_line,
                                     (sp.y * square_width) + spacing_from_line,
                                     spacing_to_line,
                                     spacing_to_line)
                         )

    # Redraw game
    pygame.display.flip()


def get_player_input():
    global user_quit

    # Op deze manier gedaan want hier pakt het altijd de laatste input
    movement_input = None
    game_input = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_input = GameInput.QUIT


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                movement_input = MovementInput.TOP
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                movement_input = MovementInput.BOTTOM
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                movement_input = MovementInput.LEFT
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                movement_input = MovementInput.RIGHT
            elif event.key == pygame.K_ESCAPE:
                game_input = GameInput.QUIT

    if movement_input is not None:
        gameboard.set_input(movement_input)

    # Het sluit nu altijd meteen af
    if game_input is not None:
        if game_input == GameInput.QUIT:
            user_quit = True

        gameboard.set_input(game_input)

def close_game():
    pygame.quit()






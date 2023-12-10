import turtle
from scoreboard import Scoreboard
from board import Board

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Tic Tac Toe")


def tic_tac_toe():
    board = Board()
    scoreboard = Scoreboard()
    continue_game = True
    while continue_game:
        screen.update()
        if board.current_player == 'x':
            screen.onclick(board.change_shape_x, btn=1)
        else:
            screen.onclick(board.change_shape_o, btn=1)
        if not board.check_rules():
            scoreboard.game_win(board.current_player)
            screen.update()
            continue_game = False
        elif '-' not in board.matrix[0] and '-' not in board.matrix[1] and '-' not in board.matrix[2]:
            scoreboard.draw()
            screen.update()
            continue_game = False


def reset_game():
    screen.reset()
    tic_tac_toe()


screen.onkey(reset_game, 'Up')
tic_tac_toe()

screen.exitonclick()
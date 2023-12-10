from turtle import Turtle, Screen

STARTING_CELL_POSITIONS = [[(-100, 100), (0, 100), (100, 100)],
                      [(-100, 0), (0, 0), (100, 0)],
                      [(-100, -100), (0, -100), (100, -100)]]

cross_shape = ((-8.5, -10), (-9.5, -10), (-0.5, -0.5), (-9.5, 10), (-8.5, 10), (0, 0.5), (8.5, 10), (9.5, 10), (0.5, 0),
               (9.5, -10), (8.5, -10), (0, -0.5))

GRID_POSITIONS = [(-50, -150), (-50, 150), (50, 150), (50, -150), (-150, -50), (150, -50), (-150, 50), (150, 50)]
screen = Screen()
screen.register_shape("cross", cross_shape)


class Board:
    def __init__(self):
        self.field = []
        self.row = []
        self.create_field()
        self.current_player = 'x'
        self.matrix = []
        self.create_result_matrix()
        self.draw_grid()

# draw grid between cells
    def draw_grid(self):
        line = Turtle()
        line.hideturtle()
        line.color("white")
        for i in range(len(GRID_POSITIONS)):
            if i % 2 == 0:
                line.penup()
                line.goto(GRID_POSITIONS[i])
            else:
                line.pendown()
                line.goto(GRID_POSITIONS[i])

# create a new cell on the game field
    def add_cell(self, position):
        new_cel = Turtle('square')
        new_cel.color('black')
        new_cel.shapesize(4, 4)
        new_cel.penup()
        new_cel.goto(position)
        self.row.append(new_cel)

# create the game field matrix 3x3
    def create_field(self):
        for row_positions in STARTING_CELL_POSITIONS:
            for position in row_positions:
                self.add_cell(position)
            self.field.append(self.row)
            self.row = []

# get cell's position on the field matrix by coordinates
    def get_cell(self, x, y):
        if y >= 60:
            if x < -40:
                return self.field[0][0]
            if x < 60:
                return self.field[0][1]
            else:
                return self.field[0][2]
        if y >= -40:
            if x < -40:
                return self.field[1][0]
            if x < 60:
                return self.field[1][1]
            else:
                return self.field[1][2]
        if y < -40:
            if x < -40:
                return self.field[2][0]
            if x < 60:
                return self.field[2][1]
            else:
                return self.field[2][2]

# replaced cell's square shape by circle shape
    def change_shape_o(self, x, y):
        cell_clicked = self.get_cell(x, y)
        if cell_clicked.shape() != 'square':
            print("You can't do this")
        else:
            cell_clicked.shape('circle')
            cell_clicked.shapesize(4, 4, 4)
            cell_clicked.color("white", "black")
            self.create_result_matrix()
            if self.check_rules():
                self.current_player = 'x'

# replaced cell's square shape by cross shape
    def change_shape_x(self, x, y):
        cell_clicked = self.get_cell(x, y)
        if cell_clicked.shape() != 'square':
            print("You can't do this")
        else:
            cell_clicked.shape('cross')
            cell_clicked.shapesize(4, 4)
            cell_clicked.color('white')
            self.create_result_matrix()
            if self.check_rules():
                self.current_player = 'o'

# create a result matrix to determine the winner
    def create_result_matrix(self):
        self.matrix = []
        matrix_row = []
        for row in self.field:
            for cell in row:
                if cell.shape() == 'cross':
                    matrix_row.append('x')
                elif cell.shape() == 'circle':
                    matrix_row.append('o')
                else:
                    matrix_row.append('-')
            self.matrix.append(matrix_row)
            matrix_row = []

# determine if there is a winner
    def check_rules(self):
        for i in range(len(self.matrix)):
            j = 0
            if self.matrix[i][j] == self.matrix[i][j + 1] == self.matrix[i][j + 2] == self.current_player or \
                    self.matrix[j][i] == self.matrix[j + 1][i] == self.matrix[j + 2][i] == self.current_player:
                return False
        if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == self.current_player or \
                self.matrix[2][0] == self.matrix[1][1] == self.matrix[0][2] == self.current_player:
            return False
        else:
            return True


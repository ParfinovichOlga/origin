from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 28, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.give_instructions()

    def give_instructions(self):
        self.goto(150, 250)
        self.color('white')
        self.write('Press ↑ to reset game', font=("Courier", 8, "normal"))

    def game_win(self, winner):
        self.goto(0, 200)
        self.color('orange')
        self.write(f"👏 {winner.capitalize()} is winner!", align=ALIGNMENT, font=FONT)

    def draw(self):
        self.goto(0, 200)
        self.color('yellow')
        self.write("🤝 X|O DRAW!", align=ALIGNMENT, font=FONT)






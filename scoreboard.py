from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",30,"normal")
MAX_SCORE = 10

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.text = "PONG GAME | created by Anan"
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 300)
        self.write("|", align=ALIGNMENT, font=FONT)
        self.goto(-180, 300)
        self.write(f"Player1 | {self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(180, 300)
        self.write(f"{self.r_score} | Player2", align=ALIGNMENT, font=FONT)
        self.goto(0,-340)
        self.write(self.text, align=ALIGNMENT, font=("Courier",20,"normal"))



    def update_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def update_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def reached_max_score(self):
        if self.l_score == MAX_SCORE or self.r_score == MAX_SCORE:
            return True
        else:
            return False

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        if self.l_score == MAX_SCORE:
            self.goto(0,-50)
            self.write("Player1 wins", align=ALIGNMENT, font=FONT)
        else:
            self.goto(0,-50)
            self.write("Player2 wins", align=ALIGNMENT, font=FONT)
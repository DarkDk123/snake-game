from turtle import Turtle
class Scoreboard(Turtle):   
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(-230, 230)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_update()
        
    def score_update(self):
        with open("E:\MY fOLDER\DARKLORD27\Programs\snake game\High Score.txt", "r") as High_Score:
            self.highscore = int(High_Score.read())
        self.clear()
        self.goto(-240, 230)
        self.write(f"SCORE: {self.score} ")
        self.goto(-240, 210)
        self.write(f"HIGH SCORE: {self.highscore + 1}")
    
    def increase_score(self):
        self.score += 1
        self.score_update()

    def game_over(self):
        self.goto(-10, 0)
        self.write("Game Over.")
        

    

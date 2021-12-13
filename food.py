from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.shapesize(0.5)
        self.penup()

        self.randposition()
        
    def randposition(self):
        self.randx = random.randint(-230, 230)
        self.randy = random.randint(-230, 230)
        self.goto(self.randx, self.randy)

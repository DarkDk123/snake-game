import turtle
STARTSIZE = 3
STARTXPOSITION = [-20, -40, -60, -80, -100, -120, -140, -160, -180, -200]
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.snake()
        self.head = self.segments[0]
    
    def snake(self):
        python1 = turtle.Turtle(shape="circle")
        python1.penup()
        python1.color("Dark Blue")
        python1.goto(0, 0)
        self.segments.append(python1)
        for body in range(STARTSIZE):
            self.add_seg(body)
            
    def add_seg(self, body):
        new_python = turtle.Turtle(shape= "square")
        new_python.speed("fastest")
        new_python.penup()
        new_python.shapesize(0.8)
        new_python.color("Green")
        new_python.goto(STARTXPOSITION[body], 0)
        self.segments.append(new_python)

    def extend(self):
        new_python = turtle.Turtle(shape= "square")
        new_python.speed("fastest")
        new_python.penup()
        new_python.shapesize(0.8)
        new_python.color("Green")
        new_python.goto(self.segments[-1].position())
        self.segments.append(new_python)

    
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg -1].xcor()
            new_y = self.segments[seg -1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(20)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)   

    def down(self):
        if self.head.heading() != UP:    
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:    
            self.head.setheading(LEFT)        
import time
import turtle
import random
from food import Food
from Snake_Class import Snake
from scoreboard import Scoreboard
screen = turtle.Screen()
screen.title("MY SNAKE GAME.")
screen.bgcolor("black")
screen.setup(height=500, width= 500)

screen.tracer(0)
snake = Snake()
scoreboard = Scoreboard()

screen.listen()
screen.onkeyrelease(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
food = Food()
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        snake.extend()
        if scoreboard.score > scoreboard.highscore:
            with open("E:\MY fOLDER\DARKLORD27\Programs\snake game\High Score.txt", "w") as write:
                write.write(f"{scoreboard.score}")
        scoreboard.increase_score()
        food.randposition()
        
    
    if snake.head.xcor() > 245 or snake.head.ycor() > 245 or snake.head.xcor() < -245 or snake.head.ycor() < -245:
        scoreboard.game_over()
        is_game_on = False
    for out in snake.segments[1:]:
        if snake.head.distance(out) <15:
            scoreboard.game_over()
            is_game_on = False
    

    
screen.exitonclick()

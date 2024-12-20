import turtle
import random
import time


screen = turtle.Screen()
screen.title("Snaik")
screen.setup(width=700, height=700)
screen.tracer(0)  
turtle.bgcolor("turquoise")


turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("black")
turtle.forward(620)
turtle.right(90)
turtle.forward(520)
turtle.right(90)
turtle.forward(620)
turtle.penup()
turtle.hideturtle()


scor = 0
delay = 0.2  
snake_size = 20


snake = turtle.Turtle()
snake.speed(0) 
snake.shape("square")
snake.penup()
snake.goto(0, 0)
snake.direction = "Stop"


food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(30, 30)


old_food = []


score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()
score.goto(0, 300)
score.write("Score: 0", align="center", font=("Courier", 24, "bold"))


def move_up():
    if snake.direction != "down":
        snake.direction = "up"

def move_down():
    if snake.direction != "up":
        snake.direction = "down"

def move_left():
    if snake.direction != "right":
        snake.direction = "left"

def move_right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + snake_size)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - snake_size)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - snake_size)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + snake_size)


screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

try:
    while True:
        screen.update()  


        if snake.distance(food) < snake_size:
            x = random.randint(-290, 270)
            y = random.randint(-240, 240)
            food.goto(x, y)
            

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("green")
            new_segment.penup()
            old_food.append(new_segment)


            scor += 10
            score.clear()
            score.write("Score: {}".format(scor), align="center", font=("Courier", 24, "bold"))


        for index in range(len(old_food) - 1, 0, -1):
            a = old_food[index - 1].xcor()
            y = old_food[index - 1].ycor()
            old_food[index].goto(a, y)

        if len(old_food) > 0:
            x = snake.xcor()
            y = snake.ycor()
            old_food[0].goto(x, y)  


        move()


        if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 240 or snake.ycor() < -240:
            time.sleep(1)  
            snake.goto(0, 0)  
            snake.direction = "Stop"  
            for fragment in old_food:
                fragment.goto(1000, 1000)  
            old_food.clear()  
            scor = 0  
            score.clear()
            score.write("Score: {}".format(scor), align="center", font=("Courier", 24, "bold"))
            delay = 0.2  


        for fragment in old_food:
            if fragment.distance(snake) < snake_size:
                time.sleep(1)  
                snake.goto(0, 0)  
                snake.direction = "Stop"  
                for fragment in old_food:
                    fragment.goto(1000, 1000)  
                old_food.clear()  
                scor = 0  
                score.clear()
                score.write("Score: {}".format(scor), align="center", font=("Courier", 24, "bold"))
                delay = 0.2  


        time.sleep(delay) 

except turtle.Terminator:
    print("Game over")

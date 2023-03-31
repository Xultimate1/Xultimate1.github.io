import turtle
import random
import time
screen = turtle.Screen()
screen.title("THE SSnakE GAMe")
screen.setup(width=700,height=700)
screen.tracer(0)
turtle.bgcolor("black")
turtle.speed(5)
turtle.pensize(1)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color("black")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()
score = 0
delay = 0.1
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("blue")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("yellow")
fruit.penup()
fruit.goto(30,30)
old_fruit = []
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("score: 0",align="center",font=("comic sans",20,"bold"))
def goUp():
    if snake.direction!="down":
        snake.direction="up"
def goDown():
    if snake.direction!="up":
        snake.direction="down"
def goLeft():
    if snake.direction!="right":
        snake.direction="left"
def goRight():
    if snake.direction!="left":
        snake.direction="right"
def snakeMove():
    if snake.direction=="up":
        y = snake.ycor()
        snake.sety(y+20)
    if snake.direction=="down":
        y = snake.ycor()
        snake.sety(y-20)
    if snake.direction=="left":
        x = snake.xcor()
        snake.setx(x-20)
    if snake.direction=="right":
        x = snake.xcor()
        snake.setx(x+20)
screen.listen()
screen.onkeypress(goUp,"Up")
screen.onkeypress(goDown,"Down")
screen.onkeypress(goLeft,"Left")
screen.onkeypress(goRight,"Right")
while True:
    screen.update()
    if snake.distance(fruit)<20:
        x = random.randint(-290,270)
        y = random.randint(-240,240)
        fruit.goto(x,y)
        scoring.clear()
        score+=1
        scoring.write("score: more than 0".format(score),align="center",font=("comic sans",20,"bold"))
        delay -= 0.001
        new_fruit = turtle.Turtle()
        snakeColor = ["red","blue","green","cyan","purple","pink","yellow","orange","violet","indigo"]
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color(random.choice(snakeColor))
        new_fruit.penup()
        old_fruit.append(new_fruit)
    for index in range(len(old_fruit)-1,0,-1):
        a = old_fruit[index-1].xcor()
        b = old_fruit[index-1].ycor()
        old_fruit[index].goto(a,b)
    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a,b)
    snakeMove()
    if snake.xcor()>339 or snake.xcor()< -350 or snake.ycor()>299 or snake.ycor()< -330:
        time.sleep(2)
        screen.clear()
        screen.bgcolor('black')
        scoring.goto(0,0)
        scoring.write("GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))
    for food in old_fruit:
        if food.distance(snake)<20:
            time.sleep(2)
            screen.clear()
            screen.bgcolor('black')
            scoring.goto(0,0)
            scoring.write("GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))
    time.sleep(delay)
turtle.Terminator()

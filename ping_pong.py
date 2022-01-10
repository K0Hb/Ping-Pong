import turtle
from random import choice, randint
# настроки окна
window = turtle.Screen()
window.title('Ping-Pong')
window.setup(width= 1.0, height= 1.0 )
window.bgcolor('black')
window.tracer(1.2)

# настроки черепахи
border = turtle.Turtle()
border.speed(0)

# заливка поля 
border.color('green')
border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()

# прорисовка линий
border.goto(0, 300)
border.color('white')
border.setheading(270)
for i in range(25):
    if i % 2 == 0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()

# создание ракеток
rocket_left = turtle.Turtle()
rocket_left.color('white')
rocket_left.shape('square')
rocket_left.shapesize(stretch_len=1, stretch_wid=5)
rocket_left.penup()
rocket_left.goto(-450, 0)

rocket_right = turtle.Turtle()
rocket_right.color('white')
rocket_right.shape('square')
rocket_right.shapesize(stretch_len=1, stretch_wid=5)
rocket_right.penup()
rocket_right.goto(450, 0)

def move_up_left():
    y = rocket_left.ycor() + 10
    if y > 240:
        y= 240
    rocket_left.sety(y + 10)

def move_down_left():
    y = rocket_left.ycor() - 10
    if y < -240:
        y= -240
    rocket_left.sety(y - 10)

def move_up_right():
    y = rocket_right.ycor() + 10
    if y > 240:
        y= 240
    rocket_right.sety(y + 10)

def move_down_right():
    y = rocket_right.ycor() - 10
    if y < -240:
        y= -240
    rocket_right.sety(y - 10)


# создание шарика 
ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.speed(5)
ball.dx = 5
ball.dy = 5
ball.penup()

window.listen()
window.onkeypress(move_up_left, 'w')
window.onkeypress(move_down_left, 's')
window.onkeypress(move_up_right, 'Up')
window.onkeypress(move_down_right, 'Down')

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.dy = -ball.dy

    if ball.ycor() <= -290:
        ball.dy = -ball.dy

    if ball.xcor() >= 490:
        ball.goto(0, randint(-150, 150))
        ball.dx = -ball.dx
        ball.dx = choice([x for x in range(1,5)])
        ball.dy = choice([x for x in range(1,5)])

    if ball.xcor() <= -490:
        ball.dx = -ball.dx
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([x for x in range(3, 8)])
        ball.dy = choice([x for x in range(3, 8)])

    if ball.ycor() >= rocket_right.ycor() - 60 and ball.ycor() <= rocket_right.ycor() + 60 \
        and ball.xcor() >= rocket_right.xcor() -6 and ball.xcor() <= rocket_right.xcor() + 6:
        ball.dx = -ball.dx

    if ball.ycor() >= rocket_left.ycor() - 60 and ball.ycor() <= rocket_left.ycor() + 60 \
        and ball.xcor() >= rocket_left.xcor() -6 and ball.xcor() <= rocket_left.xcor() + 6:
        ball.dx = -ball.dx

window.mainloop()

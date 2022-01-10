import turtle

# настроки окна
window = turtle.Screen()
window.title('Ping-Pong')
window.setup(width= 1.0, height= 1.0 )
window.bgcolor('black')

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

window.listen()
window.onkeypress(move_up_left, 'w')
window.onkeypress(move_down_left, 's')
window.onkeypress(move_up_right, 'Up')
window.onkeypress(move_down_right, 'Down')


window.mainloop()
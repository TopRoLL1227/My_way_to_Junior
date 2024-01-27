import turtle

# turtle.speed(1)

# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)

def move():
    turtle.forward(100)
    turtle.left(90)

def square():
    for i in range(4):
        move()

turtle.speed(1)
square()
turtle.goto(150, 150)
square()
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

# turtle.goto(150, 150)  # система координат

# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)

#########################################

# def move():
#     turtle.forward(100)
#     turtle.left(90)


# def drowSquare():
#     for i in range(4):
#         move()

# turtle.speed(1)

# drowSquare()
# turtle.goto(150, 150)
# drowSquare()

#########################################

# def move(size):
#     turtle.forward(size)
#     turtle.left(90)


# def drowSquare(size):
#     for i in range(4):
#         move(size)

# turtle.speed(1)

# drowSquare(60)
# turtle.goto(150, 150)
# drowSquare(120)

#########################################

def move(size):
    turtle.forward(size)
    turtle.left(90)


def drowSquare(size, color):
    for i in range(4):
        move(size, color)

def drowSquarecolor(size, color):
    turtle.color(color)
    turtle.begin_fill()
    drowSquare(size)
    turtle.end_fill()


turtle.speed(1)

drowSquarecolor(60, 'red')
turtle.goto(150, 150)
drowSquarecolor(120, 'blue')
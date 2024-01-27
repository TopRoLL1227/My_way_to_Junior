# В Python вкладені (inner) функції - це функції, які оголошені всередині іншої функції. 
# Вони доступні лише всередині області видимості зовнішньої функції та не можуть бути викликані ззовні.

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
from turtle import Turtle, Screen
screen = Screen()
jack = Turtle()


def move_forward():
    jack.forward(10)


def move_backward():
    jack.backward(10)

def move_right():
    jack_heading = jack.heading()
    jack.setheading(jack_heading - 10)

def move_left():
    jack_heading = jack.heading()
    jack.setheading(jack_heading + 10)

def clear():
    jack.clear()
    jack.penup()
    jack.home()
    jack.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey(clear, "c")
screen.exitonclick()

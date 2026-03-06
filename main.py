import turtle as t
from random import Random

t.colormode(255)
def square(self):
    self.forward(100)
    self.left(90)
    self.forward(100)
    self.left(90)
    self.forward(100)
    self.left(90)
    self.forward(100)
    self.left(90)

def dashed_line(self):
    for _ in range(15):
        self.penup()
        self.forward(10)
        self.pendown()
        self.forward(10)

def dashed_square(self):
    for _ in range(2):
        self.pendown()  # Put the pen down to start drawing a dash
        self.forward(10)
        self.penup()  # Put the pen down to start drawing a dash
        self.forward(10)
        self.pendown()  # Put the pen down to start drawing a dash
        self.forward(10)
        self.penup()  # Put the pen down to start drawing a dash
        self.forward(10)
        self.pendown()  # Put the pen down to start drawing a dash
        self.forward(10)
        self.left(90)# Draw a line segment of 10 pixels
        self.penup()  # Lift the pen up to create a gap
        self.forward(10)
        self.pendown()
        self.forward(10)
        self.penup()
        self.forward(10)
        self.pendown()
        self.forward(10)
        self.penup()
        self.forward(10)
        self.pendown()
        self.left(90)

def different_shape(self, num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        self.forward(100)
        self.right(angle)

def random_walk(self, direction, color):
    self.pensize(5)
    self.forward(30)
    self.setheading(direction)
    self.color(color)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b

def spirograph(self, size):
    for _ in range(int(360/size)):
        self.circle(150)
        self.setheading(self.heading() + size)
        self.color(random_color())
max_the_turtle = t.Turtle()
max_the_turtle.shape("arrow")
max_the_turtle.speed("fastest")
max_the_turtle.color("SkyBlue")
max_the_turtle.pencolor("Red")

random = Random()
colors = ["red","orange","yellow","green","blue",]
directions = [0,90,180,270]
# square(max_the_turtle)
# dashed_square(max_the_turtle)
# dashed_line(max_the_turtle)
# for shape_sides in range(3,11):
#     different_shape(max_the_turtle, shape_sides)
#     max_the_turtle.color(random.choice(colors))

# for _ in range(100):
#     random_walk(max_the_turtle, random.choice(directions), random.choice(colors))
# for _ in range(100):
#     random_walk(max_the_turtle, random.choice(directions), random_color())

spirograph(max_the_turtle, 90)
screen = t.Screen( )
screen.exitonclick()


import turtle
import random

random.seed(99)

turtle.setup(1200,800)
turtle.colormode(255)

turt = turtle.Turtle()
starty = turt.ycor()
turt.speed(5)

def create_forest(size):
  iterations = int(36/size)
  for i in range(iterations):
    turt.penup()
    x_value = i*1200/iterations-600
    if not (x_value > (starty-275) and x_value < (275-starty)):
      turt.setx(x_value+random.randint(-50,0))
      size = size*random.randint(95,100)/100.0
      turt.sety(starty-(size-1.25)*20+random.randint(-5,5))
      turt.pendown()
      create_tree(turt, size)


def create_tree(turt, size):
  draw_base(turt, size)
  draw_leafs(turt, size)

def draw_base(turt, size):
  turt.color('brown')
  turt.begin_fill()
  turt.setheading(0)
  turt.forward(10*size)
  turt.right(90)
  turt.forward(20*size)
  turt.right(90)
  turt.forward(10*size)
  turt.right(90)
  turt.forward(20*size)
  turt.end_fill()

def draw_leafs(turt, size, color='green', triangles=3):
  a = random.randint(50, 150)
  turt.color((0,a,0))
  for i in range(triangles):
    draw_triangle(turt, size)
    turt.sety(turt.ycor()+10*size)

def draw_triangle(turt, size):
  turt.begin_fill()
  startx = turt.xcor()
  starty = turt.ycor()
  rightside_trunk = startx + 10*size
  turt.goto(startx-20*size, starty)
  turt.goto((startx+rightside_trunk)/2.0, starty + 40 * size)
  turt.goto(rightside_trunk+20*size, starty)
  turt.goto(startx, starty)
  turt.end_fill()

def path(turt):
  turt.penup()
  turt.begin_fill()
  turt.width(5)
  turt.color('#a15c0d','#bf9a6f')
  turt.goto((0,200))
  turt.pendown()
  turt.goto((-600, -400))
  turt.goto((600,-400))
  turt.goto((0,200))
  turt.end_fill()

def green(turt):
  turt.penup()
  turt.begin_fill()
  turt.width(5)
  turt.color('#147a00','#5ba14d')
  turt.goto((0,200))
  turt.pendown()
  turt.begin_fill()
  turt.goto((600, 200))
  turt.goto((600,-400))
  turt.goto((0,200))
  turt.end_fill()
  turt.begin_fill()
  turt.goto((-600, 200))
  turt.goto((-600,-400))
  turt.goto((0,200))
  turt.end_fill()

def blue(turt):
  turt.penup()
  turt.begin_fill()
  turt.width(5)
  turt.color('#4d85a1','#7db0c9')
  turt.goto((0,200))
  turt.pendown()
  turt.begin_fill()
  turt.goto((600, 200))
  turt.goto((600,400))
  turt.goto((-600,400))
  turt.goto((-600,200))
  turt.goto((0,200))
  turt.end_fill()


green(turt)
path(turt)
blue(turt)

turt.width(2)
size = 1
for starty in [175, 100, -10, -210]:
  create_forest(size)
  size *= 1.75

turtle.done()
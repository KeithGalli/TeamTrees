import turtle
import random

turt = turtle.Turtle()
starty = turt.ycor()

def create_forest(size):
  random.seed(100)
  for i in range(10):
    turt.penup()
    turt.setx(i*100-400)
    size = random.random()*2.5
    turt.sety(starty-(size-1.25)*20)
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
  turt.color(color)
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

create_forest(5)

turtle.done()
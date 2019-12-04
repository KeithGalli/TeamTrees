import turtle
import random

BASE_WIDTH=10
BASE_HEIGHT=20

def create_tree(turt, size):
  draw_trunk(turt, size)
  draw_leafs(turt, size)

def draw_trunk(turt, size):
  trunk_width, trunk_height = (BASE_WIDTH*size, BASE_HEIGHT*size)
  turt.color('brown')
  turt.begin_fill()
  turt.setheading(0) # Head to the right
  turt.forward(trunk_width)
  turt.right(90)
  turt.forward(trunk_height)
  turt.right(90)
  turt.forward(trunk_width)
  turt.right(90)
  turt.forward(trunk_height)
  turt.end_fill()

def draw_leafs(turt, size, color='green', triangles=3):
  turt.color(color)
  for i in range(triangles):
    draw_triangle(turt, size)
    height_increase = 10*size
    turt.sety(turt.ycor() + height_increase)

def draw_triangle(turt, size):
  #triangle_width, triangle_height = (BASE_WIDTH)
  turt.begin_fill()
  startx = turt.xcor()
  starty = turt.ycor()
  rightside_trunk = startx + 10*size
  turt.goto(startx-20*size, starty)
  turt.goto((startx+rightside_trunk)/2.0, starty + 40 * size)
  turt.goto(rightside_trunk+20*size, starty)
  turt.goto(startx, starty)
  turt.end_fill()

if __name__ == '__main__':
  turt = turtle.Turtle()
  tree_size = 5
  create_tree(turt, tree_size)
  turtle.done()
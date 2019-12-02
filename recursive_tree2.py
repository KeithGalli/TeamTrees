import turtle
import random

BRANCH_COUNT = 7
TURN_ANGLE = 10

def tree(size, depth):
  if depth >= 1:
    if random.random() > 0.33:
      turt.width(depth*1.5)
      turt.color(get_color(depth))
      turt.forward(size)
      turt.right(TURN_ANGLE)
      tree(size/1.25, depth-1)
      turt.right(TURN_ANGLE)
      tree(size/1.25, depth-1)
      turt.left(3*TURN_ANGLE)
      tree(size/1.25, depth-1)
      turt.left(TURN_ANGLE)
      tree(size/1.25, depth-1)
      turt.right(2*TURN_ANGLE)
      turt.color(get_color(depth))
      turt.backward(size)

def get_color(depth):
  # Brown, Brown-Green, Green
  if BRANCH_COUNT - depth < 3:
    return 'brown'
  elif depth < 3:
    return 'green'
  else:
    return '#74871c'

if __name__ == '__main__':
  turt = turtle.Turtle()
  turt.setheading(90)
  turt.speed(0)

  turtle.colormode(255)
  tree(100, BRANCH_COUNT)
  turtle.done()
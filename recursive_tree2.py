import turtle
import random

MAX_DEPTH = 7
TURN_ANGLE = 10

def tree(size, depth):
  if depth < MAX_DEPTH:
    turt.forward(size)
    turt.right(TURN_ANGLE)
    tree(size/1.25, depth+1)
    turt.left(2*TURN_ANGLE)
    tree(size/1.25, depth+1)
    turt.right(TURN_ANGLE)
    turt.backward(size)

if __name__ == '__main__':
  turt = turtle.Turtle()
  turt.setheading(90)
  turt.speed(0)
  tree(100, 0)
  turtle.done()
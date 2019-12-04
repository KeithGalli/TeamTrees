import turtle

BRANCH_COUNT = 1
TURN_ANGLE = 30
INITIAL_BRANCH_SIZE = 100
SHRINK_FACTOR = 0.8

SPEED = 1
UP = 90

def tree(size, depth=0):
  if depth <= BRANCH_COUNT:
    turt.forward(size)
    turt.right(TURN_ANGLE)
    tree(size*SHRINK_FACTOR, depth+1)
    turt.left(2*TURN_ANGLE)
    tree(size*SHRINK_FACTOR, depth+1)
    turt.right(TURN_ANGLE)
    turt.backward(size)

if __name__ == '__main__':
  turt = turtle.Turtle()
  turt.setheading(UP)
  turt.width(4)
  turt.speed(SPEED)

  tree(INITIAL_BRANCH_SIZE)
  turtle.done()
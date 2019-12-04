import turtle
import random

class Background:
  def __init__(self, turt=turtle, WIDTH=1200, HEIGHT=800):
    self.WIDTH = WIDTH
    self.HEIGHT = HEIGHT
    self.turt = turt

    turtle.setup(WIDTH, HEIGHT)
    turtle.colormode(255)

  def color():
    green(turt)
    path(turt)
    blue(turt)

  def path(self):
    self.turt.penup()
    self.turt.begin_fill()
    self.turt.width(5)
    self.turt.color('#a15c0d','#bf9a6f')
    self.turt.goto((0,200))
    self.turt.pendown()
    self.turt.goto((-600, -400))
    self.turt.goto((600,-400))
    self.turt.goto((0,200))
    self.turt.end_fill()

  def green(self):
    self.turt.penup()
    self.turt.begin_fill()
    self.turt.width(5)
    self.turt.color('#147a00','#5ba14d')
    self.turt.goto((0,200))
    self.turt.pendown()
    self.turt.begin_fill()
    self.turt.goto((600, 200))
    self.turt.goto((600,-400))
    self.turt.goto((0,200))
    self.turt.end_fill()
    self.turt.begin_fill()
    self.turt.goto((-600, 200))
    self.turt.goto((-600,-400))
    self.turt.goto((0,200))
    self.turt.end_fill()

  def blue(self):
    self.turt.penup()
    self.turt.begin_fill()
    self.turt.width(5)
    self.turt.color('#4d85a1','#7db0c9')
    self.turt.goto((0,200))
    self.turt.pendown()
    self.turt.begin_fill()
    self.turt.goto((600, 200))
    self.turt.goto((600,400))
    self.turt.goto((-600,400))
    self.turt.goto((-600,200))
    self.turt.goto((0,200))
    self.turt.end_fill()

  def plant_trees(self):
    self.turt.width(2)
    size = 1
    for starty in [175, 100, -10, -210]:
      create_forest(size)
      size *= 1.75

  def create_forest(self):
    iterations = int(36/size)
    for i in range(iterations):
      self.turt.penup()
      x_value = i*1200/iterations-600
      if not (x_value > (starty-275) and x_value < (275-starty)):
        self.turt.setx(x_value+random.randint(-50,0))
        size = size*random.randint(95,100)/100.0
        self.turt.sety(starty-(size-1.25)*20+random.randint(-5,5))
        self.turt.pendown()
        create_tree(self.turt, size)


if __name__ == '__main__':
  # Background.planttrees()
  random.seed(99)

  turt = turtle.Turtle()
  starty = turt.ycor()
  turt.speed(5)

  turtle.done()
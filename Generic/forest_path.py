import turtle
import random

from base_tree import Tree

class Nature:
  def __init__(self, turt=turtle, WIDTH=1200, HEIGHT=800):
    self.WIDTH = WIDTH
    self.HEIGHT = HEIGHT
    self.turt = turt

    self.y_intercept = self.HEIGHT/4 # Where on the y-axis we start drawing the path
    self.slope = (self.y_intercept - (-self.HEIGHT/2))/(0 - (-self.WIDTH/2))

    # When plant_trees is called, these are the y_coordinates a row of trees are planted on
    self.tree_rows = [175, 100, -10, -210]

    turtle.setup(WIDTH, HEIGHT)
    turtle.colormode(255)

  def draw_background(self):
    self.draw_grass()
    self.draw_path()
    self.draw_sky()

  def draw_grass(self):
    self.turt.penup()
    self.turt.begin_fill()
    self.turt.width(5)
    self.turt.color('#147a00','#5ba14d')
    self.turt.goto((0,self.y_intercept))
    self.turt.pendown()
    self.turt.begin_fill()
    self.turt.goto((self.WIDTH/2, self.y_intercept))
    self.turt.goto((self.WIDTH/2,-self.HEIGHT/2))
    self.turt.goto((0,self.y_intercept))
    self.turt.end_fill()
    self.turt.begin_fill()
    self.turt.goto((-self.WIDTH/2, self.y_intercept))
    self.turt.goto((-self.WIDTH/2,-self.HEIGHT/2))
    self.turt.goto((0,self.y_intercept))
    self.turt.end_fill()

  def draw_path(self):
    self.turt.penup()
    self.turt.begin_fill()
    self.turt.width(5)
    self.turt.color('#a15c0d','#bf9a6f')
    self.turt.goto((0,self.y_intercept))
    self.turt.pendown()
    self.turt.goto((-self.WIDTH/2, -self.HEIGHT/2))
    self.turt.goto((self.WIDTH/2,-self.HEIGHT/2))
    self.turt.goto((0,self.y_intercept))
    self.turt.end_fill()

  def draw_sky(self):
    self.turt.penup()
    self.turt.begin_fill()
    self.turt.width(5)
    self.turt.color('#4d85a1','#7db0c9')
    self.turt.goto((0,self.y_intercept))
    self.turt.pendown()
    self.turt.begin_fill()
    self.turt.goto((self.WIDTH/2, self.y_intercept))
    self.turt.goto((self.WIDTH/2,self.HEIGHT/2))
    self.turt.goto((-self.WIDTH/2,self.HEIGHT/2))
    self.turt.goto((-self.WIDTH/2,self.y_intercept))
    self.turt.goto((0,self.y_intercept))
    self.turt.end_fill()

  def plant_trees(self):
    self.turt.width(2)
    size = 1
    for y_value in self.tree_rows:
      self.create_forest(size, y_value)
      size *= 1.75

  def create_forest(self, size, y_value):
    iterations = int(36/size)
    for i in range(iterations):
      self.turt.penup()
      x_value = (i*self.WIDTH/iterations)-self.WIDTH/2
      path_offset = 35*size # Used as an additional buffer so that trees don't get planted on dirt path
      on_dirt_path = (x_value > ((y_value-self.y_intercept)/self.slope)-path_offset and x_value < ((self.y_intercept-y_value)/self.slope)+path_offset)
      if not on_dirt_path:
        x_specific = x_value+random.randint(-50,0) # Add a little randomness so trees aren't too evenly spaced out
        scale = size*random.randint(95,100)/100.0 # Add slight, random variances in size
        y_specific = y_value-(size-1.25)*20+random.randint(-5,5) # Add slight, random offsets in y position for a given row
        tree = RandomGreenTree(self.turt, scale=scale, x=x_specific, y=y_specific, speed=0)
        tree.draw_tree()

# Override base Tree class and give a random green color to any tree that is created
class RandomGreenTree(Tree):
  def __init__(self, turt, x=0, y=0, scale=1, speed=3):
    super().__init__(turt, x, y, scale, speed)

    # Random green color (r, g, b)
    green_value = random.randint(50,150)
    self.color = (0, green_value, 0)

  def draw_tree(self):
    self.draw_trunk()
    self.draw_leafs(color = self.color)

if __name__ == '__main__':
  random.seed(99)
  nature = Nature()
  nature.draw_background()
  nature.plant_trees()
  turtle.done()
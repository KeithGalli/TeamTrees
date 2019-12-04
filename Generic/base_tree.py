import turtle
import random

class Tree:

  def __init__(self, turt, x=0, y=0, scale=1, speed=3):
    self.scale = scale
    self.trunk_width = 10*scale # width in pixels (default is 10 pixels)
    self.trunk_height = 20*scale

    self.turt = turt
    self.turt.speed(speed)

    # Move turtle into position
    self.turt.penup()
    self.turt.goto(x,y)
    self.turt.pendown()

  def create_tree(self):
    self.draw_trunk()
    self.draw_leafs()

  def draw_trunk(self):
    self.turt.color('brown')
    self.turt.begin_fill()
    self.turt.setheading(0) # Head to the right
    self.turt.forward(self.trunk_width)
    self.turt.right(90)
    self.turt.forward(self.trunk_height)
    self.turt.right(90)
    self.turt.forward(self.trunk_width)
    self.turt.right(90)
    self.turt.forward(self.trunk_height)
    self.turt.end_fill()

  def draw_leafs(self, color='green', triangles=3):
    self.turt.color(color)
    for i in range(triangles):
      self.draw_triangle()
      height_increase = 10*self.scale
      self.turt.sety(self.turt.ycor() + height_increase)

  def draw_triangle(self):
    branch_overhang = self.trunk_height # length branches overhang from trunk (setting it to the same value as our trunk height seemed to look good)
    triangle_height = 2*self.trunk_height # A single triangle is 2 times as tall as the trunk

    self.turt.begin_fill()

    x_init, y_init = (self.turt.xcor(), self.turt.ycor())
    x_middle = x_init + self.trunk_width/2.0
    x_bottom_left = x_init - branch_overhang 
    x_bottom_right = x_init + self.trunk_width + branch_overhang
    y_top = y_init + triangle_height

    self.turt.goto(x_bottom_left, y_init)
    self.turt.goto(x_middle, y_top)
    self.turt.goto(x_bottom_right, y_init)
    self.turt.goto(x_init, y_init)

    self.turt.end_fill()

if __name__ == '__main__':
  turtle.speed(0)
  tree = Tree(turtle, x=3, y=200, scale=5, speed=0)
  tree.create_tree()
  turtle.done()
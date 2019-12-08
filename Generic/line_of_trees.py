import turtle
import random

from base_tree import Tree

def create_forest(size, turt, y_value):
  for i in range(15):
    scale = random.random()*size
    x = i*100-600
    y = y_value + (size-1.25)*20
    tree = Tree(turt, x=x, y=y, scale=scale, speed=6)
    tree.draw_tree()

if __name__ == '__main__':
  random.seed(50)
  turt = turtle.Turtle()
  starty = 0
  create_forest(2, turt, starty)
  turtle.done()
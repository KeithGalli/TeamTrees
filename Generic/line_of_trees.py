import turtle
import random

from base_tree import Tree

random.seed(100)
starty = 0

def create_forest(size, turt):
  for i in range(10):
    size = random.random()*2.5
    x = i*100-400
    y = starty + (size-1.25)*20
    tree = Tree(turt, x=x, y=y, scale=size, speed=6)
    tree.create_tree()

if __name__ == '__main__':
  turt = turtle.Turtle()
  create_forest(5, turt)
  turtle.done()
import turtle
import random

random.seed(40)

def tree(size, turt):

  if size < 20:
    return

  turt.forward(size)

  for i in range(3):
    if random.random() > 0.25:
      left_turtle = turtle.Turtle()
      if size < 60:
        left_turtle.color('green')
      else:
        left_turtle.color('brown')
      left_turtle.width(2)
      left_turtle.shapesize(.1)
      left_turtle.speed(8)
      left_turtle.penup()
      left_turtle.setx(turt.xcor())
      left_turtle.sety(turt.ycor())
      left_turtle.pendown()
      left_turtle.setheading(turt.heading()-20+20*i)
      tree(size/1.3, left_turtle)

  # right_turtle = turtle.Turtle()
  # right_turtle.penup()
  # right_turtle.setx(turt.xcor())
  # right_turtle.sety(turt.ycor())
  # right_turtle.pendown()
  # right_turtle.setheading(turt.heading()+10)
  # tree(size/2, right_turtle)
bob = turtle.Turtle()
bob.width(5)
bob.shapesize(.1)
bob.color('brown')
bob.setheading(90)
tree(100, bob)
turtle.bgcolor('#34c0eb')
turtle.done()
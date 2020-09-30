import turtle
from random import randint
turtle.speed(0)
turtle.bgcolor('black')
x=1
while x < 300:
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)

  turtle.colormode(255)
  turtle.pencolor(b,g,r)
  turtle.fd(50 + x)
  turtle.rt(1000)
  x = x + 1

turtle.exitonclick()
import turtle

t = turtle.Turtle()

s = turtle.Screen()

list1 = ["pink","red","orange","blue","green"]

s.bgcolor("black") 

for i in range(100):
  t.color(list1[i%5])
  t.pensize(i/10+1)
  t.forward(i)
  t.left(59)
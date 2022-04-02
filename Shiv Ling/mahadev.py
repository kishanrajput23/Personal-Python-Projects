import turtle

turtle.speed(0)
turtle.hideturtle()
turtle.setup(800,600)
turtle.title('Shiva Linga')
turtle.speed(1)
turtle.up()
turtle.hideturtle()

def my_goto(x, y):
    turtle.pencolor("orange")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
   
def round_rectangle(center_x,center_y,width,height,cornersize):
    turtle.up()
    turtle.goto(center_x-width/2+cornersize,center_y-height/2)
    turtle.down()
    for _ in range(2):
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.fd(width-2*cornersize)
        turtle.circle(cornersize,90)
        turtle.fd(height-2*cornersize)
        turtle.circle(cornersize,90)
        turtle.end_fill()
    

def round_rectangle(center_x,center_y,width,height,cornersize):
    turtle.up()
    turtle.goto(center_x-width/2+cornersize,center_y-height/2)
    turtle.down()
    for _ in range(2):
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.fd(width-2*cornersize)
        turtle.circle(cornersize,90)
        turtle.fd(height-2*cornersize)
        turtle.circle(cornersize,90)
        turtle.end_fill()
        
round_rectangle(0,0,200,300,80)   

turtle.fillcolor('black')
turtle.begin_fill()



turtle.goto(-35, 40)
turtle.penup()
turtle.fillcolor('white')
turtle.begin_fill()
turtle.forward(80)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(10)
turtle.left(90)


turtle.goto(-35, 80)
turtle.forward(80)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(10)
turtle.left(90)

turtle.goto(-35, 60)
turtle.forward(80)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(10)
turtle.left(90)

turtle.pendown()
turtle.end_fill()


turtle.fillcolor('red')
turtle.begin_fill()

turtle.goto(5,50)
turtle.penup()
r = 15
turtle.circle(r)
turtle.pendown()
turtle.end_fill()

turtle.goto(-150, -175)
turtle.penup()
turtle.pencolor("black")
turtle.fillcolor("black")
turtle.begin_fill()
round_rectangle(90,-125,600,100,50) 
turtle.pendown()


my_goto(-300, -300)
turtle.write('BY :- Coding_Buddies4', font=("Bradley Hand ITC", 50, "bold"))  


my_goto(-150,150)
turtle.write('हर हर महादेव', font=("Bradley Hand ITC", 50, "bold"))  
turtle.done()
import turtle
t = turtle.Turtle()
t.speed(0)

colors = ["red","blue","green","yellow","purple","orange"]
 
for i in range(100):
    t.pencolor(colors[i % 6])
    t.circle(80)
    t.left(5) 

turtle.done()
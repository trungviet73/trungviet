#bai8.1
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

painter = turtle.Turtle()
painter.fillcolor('blue')
painter.pencolor('blue')
painter.pensize(3)

def drawsq(t, s):
    for i in range(4):
        t.forward(s)
        t.left(90)

for i in range(1,180):
    painter.left(18)
    drawsq(painter, 200)

#bai8.2
import turtle, random
colors = ["red","green","blue","orange","purple","prink","yellow"]
painter = turtle.Turtle()
painter.pensize(3)
for i in range(10):
    color = random.choice(colors)
    painter.pencolor(color)
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0, 0)

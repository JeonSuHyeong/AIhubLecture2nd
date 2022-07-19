import math
import turtle as t

"""
t.penup()
t.goto(-720,0)
t.pendown()
for x in range(-720,720):
    t.goto(x,math.sin(math.radians(x))*100)

t.done()
"""
def draw(head, dist):
    t.setheading(head)
    t.forward(15)


def toleft():
    draw(180,15)

def toright():
    draw(0,15)

def toup():
    draw(90,15)

def todown():
    draw(270,15)



t.shape("turtle")
t.speed(10)
t.onkeypress(toleft, "Left") #(함수명, 키보드이름(정해져잇다))
t.onkeypress(toright, "Right")
t.onkeypress(toup, "Up")
t.onkeypress(todown, "Down")
t.listen()

t.done()
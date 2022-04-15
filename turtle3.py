from turtle import *

width(4)

forward(200)
right(90)

pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)

goto(100, 100)


def drawStar(x, y):
    pu()
    goto(x, y)
    pd()
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)


for x in range(0, 250, 50):
    drawStar(x, 0)

# goto(100, 400)

colormode(255)
lt(90)
lv = 14
l = 120
s = 45

width(lv)
r = 0
g = 0
b = 0
pencolor(r, g, b)
penup()
bk(l)
pendown()
fd(l)


def draw_tree(l, level):
    global r, g, b
    w = width()
    width(w*3.0 / 4.0)
    r = r+1
    g = g+2
    b = b+3
    pencolor(r % 200, g % 200, b % 200)
    l = 3.0/4.0*l

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level+1)
    bk(l)
    rt(2*s)
    fd(l)

    if level < lv:
        draw_tree(l, level+1)
    bk(l)
    lt(s)
    width(w)


speed('fastest')
draw_tree(l, 4)

done()

import turtle, time

wn = turtle.Screen()
wn.setup(800, 900, 100, 0)
wn.bgcolor('orange')
turtle.tracer(3)


def object(primitive, w, h, clr, x, y):
    t = turtle.Turtle(primitive)
    t.up()
    t.shapesize(w, h)
    t.color(clr)
    t.goto(x, y)
    return t


head = object('circle', 12, 12, 'gold', 0, 0)
eye1 = object('circle', 2, 2, 'white', -50, 35)
eye2 = object('circle', 2, 2, 'white', 50, 35)
pupil1 = object('circle', 1.3, 0.8, 'black', -50, 35)
pupil2 = object('circle', 1.3, 0.8, 'black', 50, 35)
pupil3 = object('circle', 1.3, 0.8, 'gray', -50, 35)
pupil4 = object('circle', 1.3, 0.8, 'gray', 50, 35)
mouth1 = object('circle', 2, 6, 'red', 0, -50)
mouth2 = object('circle', 1.5, 5, 'pink', 0, -50)
hat = object('triangle', 10, 10, 'green', 0, 140)
nose = object('triangle', 1.5, 1.5, 'orange', 0, 0)
arm1 = object('square', 10, 2, 'blue', -50, -190)
arm2 = object('square', 10, 2, 'blue', 50, 190)
arm1.right(45)
arm2.left(45)
leg1 = object('square', 10, 2, 'red', -30, -300)
leg2 = object('square', 10, 2, 'red', 30, -300)
body = object('circle', 11, 8, 'blue', 0, -210)
hat.left(90)
nose.rt(90)

turtle.tracer(1)
while True:
    arm1.right(45)
    arm2.left(45)
    arm1.setposition(-50, -190)
    arm2.setposition(50, -190)
    time.sleep(0.5)
    arm1.left(45)
    arm2.right(45)
    pupil3.hideturtle()
    pupil4.showturtle()
    hat.goto(0, 200)
    time.sleep(0.1)
    pupil4.hideturtle()
    pupil3.showturtle()
    hat.goto(0, 140)
    time.sleep(0.1)
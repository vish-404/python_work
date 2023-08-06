import turtle, time
turtle.title("R3")
b =  turtle.Turtle()

s = turtle.Screen()

#to change the turtle display 
turtle.setworldcoordinates(-40, -40, 480, 480)  # (llx,lly,urx,ury)
# llx – a number, x-coordinate of lower left corner of canva
# lly – a number, y-coordinate of lower left corner of canvas
# urx – a number, x-coordinate of upper right corner of canvas
# ury – a number, y-coordinate of upper right corner of canvas

s.bgcolor("black")
b.speed(0)

b.forward(100)  # 100 pixels ,,,    backward() // bk()  for back
b.left(60)  # 60 degree  ,,, lt()  /// rt() or right()
b.fd(100)  # same as forward
b.rt(45)
b.back(200)
print(b.position(), b.heading)   # for position and heading direction
b.setposition(200, -100) 

b.color('red', 'yellow')
b.speed(0)
b.begin_fill()
for _ in range(36):
    b.fd(200)
    b.lt(170)
b.end_fill()

turtle.delay(1000)

b.dot()
b.goto(0, 0)
b.dot(20, "blue") 
b.circle(50, 270)  # radius, arc-angle
print(b.position(), b.heading(), b.towards(0,0))
print(round(b.xcor(), 5)) 

b.clear()




turtle.done()  # to let the window on after completion of the task
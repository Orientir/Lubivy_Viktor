import turtle

screen = turtle.Screen()
screen.title("My first window")

pen = turtle.Turtle()
pen.shape("turtle")
pen.color("green")
pen.speed(1)
# pen.hideturtle()

figure = input("Input figure on keyboard ")

if figure == "circle":
    pen.circle(100)
elif figure == "square":
    pen.begin_fill()
    pen.left(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.end_fill()
else:
    pen.penup()
    pen.backward(150)
    pen.write(f"You choose {figure}. We do not draw this figure. Try again", font=('Arial', 14, 'normal'))
    new_figure = input("Try again ")

    pen.pendown()

    if new_figure == "circle":
        pen.clear()
        pen.circle(100)
    elif new_figure == "square":
        pen.clear()
        pen.begin_fill()
        pen.left(90)
        pen.forward(100)
        pen.right(90)
        pen.forward(100)
        pen.right(90)
        pen.forward(100)
        pen.right(90)
        pen.forward(100)
        pen.end_fill()
    else:
        pen.penup()
        pen.backward(150)
        pen.write(f"You choose {figure}. We do not draw this figure. Try again", font=('Arial', 14, 'normal'))
        new_figure = input("Try again ")

screen.mainloop()
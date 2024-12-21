import turtle
x_co=int(input("Please input x axis: "))
y_co=int(input("Please Input y-axis: "))
size_int=int(input("Please input the size of one mside of the octogon: "))
def draw_octagon(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown() 
    for _ in range(8):
        turtle.forward(size)
        turtle.left(45)


screen = turtle.Screen()
screen.title("Octagon Drawing")
draw_octagon(x_co, y_co, size_int)
screen.mainloop()


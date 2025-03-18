import turtle
turtle.speed(0)
turtle.ht()

# Parameters
recursion_depth = 8  # Square's length (a power of 2)
scale =  6           # Scale for the drawing

# Draws a square with center (x, y) and the length r
def draw_square(x, y, r):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.forward(r/2)
    turtle.left(90)
    turtle.forward(r/2)
    turtle.left(90)
    turtle.pendown()
    turtle.fillcolor('lime')
    turtle.begin_fill()
    for dummy_index in range(4):
        turtle.forward(r)
        turtle.left(90)
    turtle.penup()    
    turtle.setposition(x, y)
    turtle.left(180)
    turtle.end_fill()

# Main recursive function
def fractal_star(x, y, r):    
    if (int(r) <= 0):  # Termination condition
        return
    else:
        fractal_star(x-r,y+r,r/2) # recursive call:  upper left corner, half radius
        fractal_star(x+r,y+r,r/2) # recursive call: upper right corner, half radius
        fractal_star(x-r,y-r,r/2) # recursive call:  lower left corner, half radius
        fractal_star(x+r,y-r,r/2) # recursive call: lower right corner, half radius
        draw_square(scale * x, scale * y, scale * r)

# Call recursive function
fractal_star(0,0,recursion_depth)

turtle.mainloop()

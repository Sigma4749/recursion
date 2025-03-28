import turtle
from random import randint

# Parameters
m = 8       # Grid dimension (a power of 2)
scale = 10  # Scale for the drawing
colors = [(1,1,1),(0,0,0),(0.910,0.695,0.818),(0.570,0.751,0.905),(0.705,0.540,0.754),(1,0.996,0.716)] # List of colors
turtle.speed(0) # Animation speed
turtle.ht()     # Hide drawing tool

# Auxiliary function for drawing
def draw_square(x,y,length, color):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.forward(length/2)
    turtle.left(90)
    turtle.forward(length/2)
    turtle.left(90)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for dummy_index in range(4):
        turtle.forward(length)
        turtle.left(90)
    turtle.penup()    
    turtle.setposition(x, y)
    turtle.left(180)
    turtle.end_fill()    

# Creates the chessboard to tile
def create_chessboard(m):
    grid = [ [0 for i in range(m)] for j in range(m) ] # Initialization
    grid[randint(0,m-1)][randint(0,m-1)] = 1   # Marks one square of the grid at random
    for dummy_index in range(m): # Shows grid on terminal
        print(grid[dummy_index])
    print("")
    return grid

# Main recursive function
def grid_tessellation(grid, x, y):
    n = int(len(grid)/2)

    # Termination condition
    if n <= 1:
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 0:
                    grid[i][j] = ((x+y) % 3)+2
        draw_square(scale*(x-1), scale*(y+1), 2*scale, colors[grid[0][0]])
        draw_square(scale*(x+1), scale*(y+1), 2*scale, colors[grid[0][1]])
        draw_square(scale*(x-1), scale*(y-1), 2*scale, colors[grid[1][0]])
        draw_square(scale*(x+1), scale*(y-1), 2*scale, colors[grid[1][1]])
        return

    # Recursive part
    square1 = [ grid[i][0:n] for i in range(n)  ]    
    square2 = [ grid[i][n:len(grid)] for i in range(n)  ]
    square3 = [ grid[i][0:n] for i in range(n,len(grid))  ]
    square4 = [ grid[i][n:len(grid)] for i in range(n,len(grid))  ]

    # Searchs for the quadrant which contains the marked square
    erased_square_quadrant = -1
    for i in range(len(grid)):
        for j in range(len(grid)):
            if i < len(grid)/2:
                if j < len(grid)/2:
                    if (grid[i][j] != 0):
                        erased_square_quadrant = 1
                        break
                else:
                    if (grid[i][j] != 0):
                        erased_square_quadrant = 2
                        break
            else:
                if j < len(grid)/2:
                    if (grid[i][j] != 0):
                        erased_square_quadrant = 3
                        break
                else:
                    if (grid[i][j] != 0):
                        erased_square_quadrant = 4
                        break

    # Colors the three incindent squares on the other quadrants
    if (erased_square_quadrant == 1):
        square2[n-1][0] = 5
        square3[0][n-1] = 5
        square4[0][0] = 5
    elif(erased_square_quadrant == 2):
        square1[n-1][n-1] = 5
        square3[0][n-1] = 5
        square4[0][0] = 5
    elif(erased_square_quadrant == 3):
        square1[n-1][n-1] = 5
        square2[n-1][0] = 5
        square4[0][0] = 5
    else:
        square1[n-1][n-1] = 5
        square2[n-1][0] = 5
        square3[0][n-1] = 5

    # Recursive calls
    grid_tessellation(square1, x-n, y+n)
    grid_tessellation(square2, x+n, y+n)
    grid_tessellation(square3, x-n, y-n)
    grid_tessellation(square4, x+n, y-n)


# Main function: creates a random chessboard and tiles it with L-shapes
if __name__ == "__main__":
    grid = create_chessboard(m)
    grid_tessellation(grid, int(len(grid)/2),int(len(grid)/2))
    turtle.mainloop()

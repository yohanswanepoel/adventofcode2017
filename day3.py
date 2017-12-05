import sys
import csv

def day3():
    puzzle_size =289326
    #puzzle_size = 47
    matrix_size = 539
    calc(puzzle_size, matrix_size)

def calc( puzzle_size, matrix_size ):
    # matrix = [[0 for x in range(matrix_size)] for y in range(matrix_size)]
    center = (539 - 1) / 2
    width = 1
    counter = 1
    corner = 0
    x = 0
    y = 0
    val = 0
    prev = 0
    x_dir = 'N'
    y_dir = 'N'
    y_top = 0
    y_bottom = 0
    x_left = 0
    x_right = 0
    # start walking the matrix
    found = False
    steps = 0
    while(not(found)):
        prev = val
        val += 1
        corner = (width * width)

        if(val == puzzle_size):

            found = True
            print("Found x=", x," y=", y)
            steps = abs(x) + abs(y)
            print("Steps",steps)
            break
        if (corner == val):
            x += 1 # Step one to the right
            y_dir = 'U'
            x_dir = 'N'
            width = width + 2 # Double the width
            y_top = int(-(width - 1) / 2)
            y_bottom = int((width - 1) / 2)
            x_left = int(-(width - 1) / 2)
            x_right = int((width - 1) / 2)
        else:
            #print("Y t b ",y_top,y_bottom)
            #print("X l r ",x_left,x_right)
            #print("Cur x y ",x,y)
            if((y_top == y) and (x_right == x)): # Top Right Corner go left
                y_dir = 'N'
                x_dir = 'L'

            if ((y_top == y) and (x_left == x)):  # Top Left Corner go Down
                y_dir = 'D'
                x_dir = 'N'

            if ((y_bottom == y) and (x_left == x)):  # Bottom Left Corner go Right
                y_dir = 'N'
                x_dir = 'R'

            if ((y_bottom == y) and (x_right == x)):  # Bottom Right New loop taken above
                y_dir = 'Y'
                x_dir = 'N'

            #print(x_dir,y_dir)

            if(x_dir == 'L'):
                x -= 1
            if(x_dir == 'R'):
                x += 1
            if(y_dir == 'U'):
                y -= 1
            if (y_dir == 'D'):
                y += 1




if __name__ == '__main__':
    day3()
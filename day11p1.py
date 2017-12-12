import sys
import operator

def start_game():
    with open('day11.txt') as f:
        trail_string = f.read()
    #trail_string = "n,s,nw,sw,ne,se"
    trail_steps = trail_string.split(',')
    print("Steps walked: ",len(trail_steps))
    where_am_i = map_route(trail_steps)

    print("where am i",where_am_i)

    least_steps = steps_to_home(where_am_i)
    #least_steps = steps_to_home((0,6))
    print("Least Steps: ",least_steps)
    least_steps = steps_to_home_using_math(where_am_i)
    print("Least Steps: ", least_steps)


def steps_to_home_using_math(where_am_i):
    row = where_am_i[0]
    col = where_am_i[1]
    steps = 0

    if (abs(row) < abs(col)):
        steps = abs(row) + int((abs(col) - abs(row) )/2)
    elif (abs(row) > abs (col)):
        steps = abs(col) + int((abs(row) - abs(col) ) / 2)
    else:
        steps = abs(row)
    return steps

def steps_to_home(where_am_i):
    HOME_ROW = 0
    HOME_COL = 0
    row = where_am_i[0]
    col = where_am_i[1]
    steps = 0
    # Always move diagonal until column or row is aligned with start
    while col != HOME_COL:

        if col > HOME_COL:  #GO NW
            col -= 1
        else:
            col += 1
        if row < HOME_ROW: # GO SW
            row += 1
        elif row > HOME_ROW: # GO NE
            row -= 1
        else: # JUST GO diagonal anywhere
            row += 1

        steps += 1

    print ("r,c",row,col)
     # Then move up or down
    while row != HOME_ROW:
        if row > HOME_ROW:# GO N
            row -= 2
        else:  # GO S
            row += 2

        steps += 1

    return steps

def map_route(trail_steps):
    # North, South direction is 2 rows
    # NE,SE,NW,SW is 1 row and 1 col
    # 0,0 center of my board
    #             N0,-2
    #      NW-1,-1   NE-1,1
    #             0,0
    #      SW1,-1   SE1,1
    #            S0,2
    #
    max_distance = 0

    NORTH = "n"
    SOUTH = "s"
    NORTH_EAST = "ne"
    SOUTH_EAST = "se"
    NORTH_WEST = "nw"
    SOUTH_WEST = "sw"

    row = 0
    col = 0

    for s in trail_steps:
        if  s == NORTH: #COL -2
            row -= 2
        elif s == SOUTH: #COL +2
            row += 2
        elif s == SOUTH_EAST:
            col += 1
            row += 1
        elif s == SOUTH_WEST:
            col -= 1
            row += 1
        elif s == NORTH_EAST:
            col += 1
            row -= 1
        elif s == NORTH_WEST:
            col -= 1
            row -= 1
        dist = steps_to_home((row, col))

        if (dist > max_distance):
            max_distance = dist

    print("MAX:", max_distance)

    return(row,col)

if __name__ == '__main__':
    start_game()

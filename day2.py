import sys

def day2():
    w, h = 4, 3;
    matrix = [[None for x in range(w)] for y in range(h)]
    matrix[0][0] = 5
    matrix[0][1] = 1
    matrix[0][2] = 9
    matrix[0][3] = 5

    matrix[1][0] = 7
    matrix[1][1] = 5
    matrix[1][2] = 3
    matrix[1][3] = None

    matrix[2][0] = 2
    matrix[2][1] = 4
    matrix[2][2] = 6
    matrix[2][3] = 8

    calc(matrix)

def calc( matrix ):
    print ("Matrix: ", matrix)
    checksum = 0
    minv = 0
    maxv = 0
    for row in matrix:
        print(row)
        minv = min(v for v in row if v is not None)
        maxv = max(v for v in row if v is not None)
        checksum = checksum + (maxv - minv)
    print("Checksum",checksum)

if __name__ == '__main__':
    day2()
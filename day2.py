import sys
import csv

def day2():
    w, h = 16, 16;
    matrix = [[None for x in range(w)] for y in range(h)]

    datafile = open('day2.csv', 'r')
    datareader = csv.reader(datafile, delimiter=',')
    matrix = []
    tmprow = []
    for row in datareader:
        print("ROW",row)
        tmprow=[]
        for v in row:
            tmprow.append(int(v))
        matrix.append(tmprow)
        print(matrix)
    calc(matrix)

def calc( matrix ):
    # print ("Matrix: ", matrix)
    checksum = 0
    minv = 0
    maxv = 0
    for row in matrix:
        print(row)
        minv = min(v for v in row if v is not None)
        maxv = max(v for v in row if v is not None)
        print("Min",minv)
        print("Max",maxv)
        print("Dff",(maxv-minv))
        checksum = checksum + (maxv - minv)
    print("Checksum",checksum)

if __name__ == '__main__':
    day2()
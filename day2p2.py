import sys
import csv

def day2():
    w, h = 16, 16;
    matrix = [[None for x in range(w)] for y in range(h)]

    datafile = open('day2p2.csv', 'r')
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
        col_counter = 0
        while col_counter < len (row):
           col_walker = 0
           for x in row:
               if col_counter != col_walker:
                   if (int(row[col_walker]) % int(row[col_counter])) == 0:
                       val = (int(row[col_walker]) / int(row[col_counter]))
                       checksum += val
               col_walker += 1
           col_counter += 1
    print("Checksum",checksum)

if __name__ == '__main__':
    day2()
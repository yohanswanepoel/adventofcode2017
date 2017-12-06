import sys

def day4():


    valid_lines=0
    with open('day4p2.txt') as f:
        mylist = f.read().splitlines()

    for line in mylist:
        valid_lines += testvalid(line)
    print(valid_lines)


def testvalid( seq_str ):

    arr = seq_str.split(' ')
    arr = sortwords(arr)
    print (len(arr) == len(set(arr)))
    print (len(arr),len(set(arr)))
    print (arr)
    print (set(arr))
    return (len(arr) == len(set(arr)))

def sortwords(line):
    newArr = []
    for w in line:
        newArr.append(sortword(w))
    return newArr

def sortword(word):
    return ''.join(sorted(word))

if __name__ == '__main__':
    day4()
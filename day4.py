import sys

def day4():


    valid_lines=0
    with open('day4.txt') as f:
        mylist = f.read().splitlines()

    for line in mylist:
        valid_lines += testvalid(line)
    print(valid_lines)


def testvalid( seq_str ):
    arr = seq_str.split(' ')
    print (len(arr) == len(set(arr)))
    print (len(arr),len(set(arr)))
    print (arr)
    print (set(arr))
    return (len(arr) == len(set(arr)))


if __name__ == '__main__':
    day4()
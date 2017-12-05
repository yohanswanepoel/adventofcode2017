import sys

def day1():
    if len(sys.argv) == 2:
        sequence = sys.argv[1]
        calc(sequence)
    else:
        print("No Args passed in")

def calc( seq_str ):
    print ("String: ", seq_str)
    prev = None
    first = None
    sum = 0
    for x in seq_str:
        if first is None:
            first = x
        if prev == x:
            print("Match")
            sum += int(x)
        prev = x
    if prev == first:
        print ("Last = First")
        sum += int(first)

    print ("Result: ", sum)

if __name__ == '__main__':
    day1()
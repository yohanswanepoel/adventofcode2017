import sys

def day1():
    if len(sys.argv) == 2:
        sequence = sys.argv[1]
        #sequence = '12131415'
        calc(sequence)
    else:
        print("No Args passed in")

def calc( seq_str ):
    print ("String: ", seq_str)
    prev = None
    first = None
    sum = 0
    jump = int(len(seq_str)/2)
    walker = 0
    seq_len = len(seq_str)

    for x in seq_str:

        if walker + jump < seq_len:
            print("x c",x,seq_str[walker + jump])
            if x == seq_str[walker + jump]:
                sum += int(x)
        else:
            if x == seq_str[(walker + jump) - seq_len]:
                sum += int(x)
        walker += 1
    print ("Result: ", sum)

if __name__ == '__main__':
    day1()
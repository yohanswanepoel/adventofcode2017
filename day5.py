import sys

def day5():
    steps = [0,3,0,1,-3]
    steps = []
    with open('day5.txt') as f:
        mylist = f.read().splitlines()
    for l in mylist:
        steps.append(int(l))
    print (steps)
    performTask(steps)

def performTask( steps ):
    step_counter = 0
    current_instruction = 0
    next_instruction = 0
    size = len(steps)
    while(True):
        if(current_instruction < len(steps) and current_instruction > -1):
            step_counter += 1
            next_instruction += steps[current_instruction]
            steps[current_instruction] += 1
            current_instruction = next_instruction
        else:
            break
    print(step_counter)

if __name__ == '__main__':
    day5()
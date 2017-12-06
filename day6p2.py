import sys

def day6():

    bank = []
    with open('day6p1.txt') as f:
        mylist = f.read().splitlines()
    for l in mylist:
        bank.append(int(l))

    #bank = [0, 2, 7, 0]
    print(bank)
    performTask(bank)

def performTask( bank ):
    bank_history = []
    bank_history_string = ''.join(map(str, bank))
    bank_history.append(bank_history_string)
    print(bank_history)
    unique = True
    counter = 0
    times_found = 0
    first_duplicate = ""
    while unique:
        counter += 1
        bank = redistribute(bank)
        bank_history_string = ''.join(map(str, bank))
        #print(bank_history_string)
        #print(bank_history)
        if bank_history_string == first_duplicate:  #Python is Awesome!!!
            print("History",bank_history_string)
            break

        if bank_history_string in bank_history and times_found == 0: #First Find
            first_duplicate = bank_history_string
            print("First Duplicate", first_duplicate)
            times_found += 1
            counter = 0 #Reset the counter
        else:
            bank_history.append(bank_history_string)

    print("Counter: ", counter)

def redistribute(bank):
    location_of_highest_register = bank.index(max(bank))
    next_register = location_of_highest_register + 1
    value_to_redistribute = bank[location_of_highest_register]
    bank[location_of_highest_register] = 0  # ZERO out the register

    # Redistribute
    while value_to_redistribute > 0:
        if next_register >= len(bank):
            next_register = 0

        bank[next_register] += 1
        next_register += 1
        value_to_redistribute -= 1


    return(bank)
if __name__ == '__main__':
    day6()
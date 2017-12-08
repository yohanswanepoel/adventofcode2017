import sys
import operator

def start_game():
    with open('day8.txt') as f:
        lines = f.read().splitlines()

    register_bank = seed_register(lines)
    #print(register_bank)
    final_register_bank = do_calculations(register_bank,lines)
    print(final_register_bank)
    get_highest_value_register(final_register_bank)

def get_highest_value_register(final_register_bank):
    print(max(final_register_bank.items(),key=operator.itemgetter(1))[1])

def do_calculations(register_bank,instructions):
    # Instruction at 1
    # Register acted on at 0
    # Amount of action 2
    # Register to Compare at 4
    # Comparitor at 5
    # Value to Compare at 6
    for i in instructions:
        instruction = i.split(' ')
        if test_condition(register_bank,instruction):
            register_bank = perform_action(register_bank,instruction)

    return register_bank


    return register_bank

def perform_action(register_bank,instruction):
    operator = instruction[1]
    register = instruction[0]
    register_value = register_bank[register]
    value = int(instruction[2])

    if operator == 'inc':
        register_value += value
        register_bank[register] = register_value
    elif operator == 'dec':
        register_value -= value
        register_bank[register] = register_value
    else:
        raise ValueError('Invalid Operator Specified')
    return register_bank

def test_condition(register_bank,instruction):
    comparitor = instruction[5]
    register = instruction[4]
    register_value = register_bank[register]
    value = int(instruction[6])
    if comparitor == '>':
        return register_value > value
    elif comparitor == '<':
        return register_value < value
    elif comparitor == '>=':
        return register_value >= value
    elif comparitor == '==':
        return register_value == value
    elif comparitor == '<=':
        return register_value <= value
    elif comparitor == '!=':
        return register_value != value
    else:
        raise ValueError('Invalid Comparitor Specified')




def seed_register(lines):
    register_bank = {}
    for l in lines:
        line_tokens = l.split(' ')
        register_bank[line_tokens[0]] = 0   #register at 0
        register_bank[line_tokens[4]] = 0   #register at 4
    return register_bank

if __name__ == '__main__':
    start_game()

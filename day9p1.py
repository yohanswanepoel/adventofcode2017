import sys
import operator

def start_game():
    with open('day9.txt') as f:
        stream = f.read()
    process_stream(stream)

class Token_Stack:
    def __init__(self):
        self.tokens=[]

    def is_empty(self):
        return self.tokens == []

    def push(self,item):
        self.tokens.append(item)

    def pop(self):
        return self.tokens.pop()

    def peek(self):
        if self.size() == 0:
            return None
        return self.tokens[len(self.tokens) - 1]

    def size(self):
        return len(self.tokens)


def process_stream(stream):
    GROUP_OPEN = 1
    GARBAGE_OPEN = 3
    token_stack = Token_Stack()
    ignore_next = False
    counter = 0
    for token in stream:
        if ignore_next:  #Ignore the next token and reset Ignore next rule
            ignore_next = False
        else:
            if (token == '!'):  #Ignore next
                #print("Ignore")
                ignore_next = True
            elif token == "{" and token_stack.peek() != GARBAGE_OPEN: # Open a group if not in garbage
                #print("Open Group")
                token_stack.push(GROUP_OPEN)
            elif token == "}" and token_stack.peek() == GROUP_OPEN and token_stack.peek() != GARBAGE_OPEN: #Close a group if an open group exists and not in garbage
                #print("Close Group",token_stack.size())
                counter += token_stack.size()
                token_stack.pop()
            elif token == "<" and token_stack.peek() != GARBAGE_OPEN:
                #print("Open Garbage")
                token_stack.push(GARBAGE_OPEN)
            elif token == ">" and token_stack.peek() == GARBAGE_OPEN:
                #print("Close Garbage")
                token_stack.pop()
        #print(token_stack.tokens)
    print(counter)



if __name__ == '__main__':
    start_game()

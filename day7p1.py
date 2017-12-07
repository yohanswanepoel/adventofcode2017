import sys

def day7():

    nodes = []
    node_children = []
    leafNodes = []
    with open('day7p1.txt') as f:
        lines = f.read().splitlines()
    for l in lines:
        if "->" in l:
            nodes.append(l.split(' ')[0])
            node_children.append(l.split('->')[1])
        else:
            leafNodes.append(l.split(' ')[0])

    #bank = [0, 2, 7, 0]

    print(nodes)
    print(leafNodes)
    print(node_children)
    #performTask(bank)
    found_root = 0
    for n in nodes:
        found_root = 0
        for nc in node_children:
            if n in nc:
                found_root += 1
        if found_root == 0:
            print("Root",n)

if __name__ == '__main__':
    day7()

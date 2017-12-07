import sys
from anytree import Node, RenderTree


def getNodeProperties(l):
    node_name = l.split(' ')[0].strip()
    node_weight = l.split('(')[1].split(')')[0]
    node_children = []
    node_children_str = ""
    if("->" in l):
        node_children_str = (l.split('->')[1])
        node_children = node_children_str.split(',')
    node = {node_name : {'weight':node_weight,'children':node_children}}
    return node

def findRoot(node_children,nodes):
    found_root = 0
    for n in nodes:
        found_root = 0
        for nc in node_children:
            if n in nc:
                found_root += 1
        if found_root == 0:
            return(n)

def day7():

    nodes = []
    node_children = []
    tmp_nodes = {}
    tree = {}
    leafNodes = []
    with open('day7p1sample.txt') as f:
        lines = f.read().splitlines()
    for l in lines:
        node = getNodeProperties(l)

        tmp_nodes.update(node)
        if "->" in l:
            nodes.append(l.split(' ')[0])
            node_children.append(l.split('->')[1])
            node_name = l.split(' ')[0]
            node_weight = l.split('(')[1].split(')')[0]
            #tmp_nodes[l.split(' ')[0]] = {}
        else:
            node_name = l.split(' ')[0]
            node_weight = l.split('(')[1].split(')')[0]


    #bank = [0, 2, 7, 0]
    print(tmp_nodes)
    print(nodes)
    print(leafNodes)
    print(node_children)
    #performTask(bank)
    my_tree = {}
    root = findRoot(node_children,nodes)
    print("Root",root)
    # Determine Towers

    print("weight",add_weights(root,tmp_nodes))
    check_weights(root,tmp_nodes)
    build_tree(root,tmp_nodes,None)
    #print("My Tree",tmp_nodes)

def check_weights(root,tmp_nodes):
    root_node = tmp_nodes[root]
    weight = int(root_node['weight'])

    print("Printing Child weights",root,root_node,weight)
    child_nodes = root_node['children']
    node_children_weight = 0
    for child in child_nodes:
        child_name = child.strip()
        print(child_name,tmp_nodes[child_name]['total_weight'])

def build_tree(root,tmp_nodes,parent):
    root_node = tmp_nodes[root]
    weight = int(root_node['weight'])

    print("ROOT",root,root_node,weight)
    child_nodes = root_node['children']
    node_children_weight = 0
    for child in child_nodes:
        child_name = child.strip()
        build_tree(child_name,tmp_nodes,root)


def add_weights(root,tmp_nodes):
    root_node = tmp_nodes[root]
    weight = int(root_node['weight'])

    child_nodes = root_node['children']
    node_children_weight = 0
    for child in child_nodes:
        child_name = child.strip()
        if (len(tmp_nodes[child_name]['children']) == 0): #This is a child node
            node_children_weight += int(tmp_nodes[child_name]['weight'])
        else:
            add_weights(child_name,tmp_nodes)
    total_weight = node_children_weight + weight
    tmp_nodes[root]['total_weight'] = total_weight
    tmp_nodes[root]['children_weight'] = node_children_weight



if __name__ == '__main__':
    day7()

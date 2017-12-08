import sys
from treelib import Node, Tree


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


    my_tree = Tree()
    my_dict_tree = {}
    root = findRoot(node_children,nodes)
    print("Root",root)
    # Determine Towers

    print("weight",add_weights(root,tmp_nodes))
    check_weights(root,tmp_nodes)
    tree_dict = {}
    jtree = None
    build_tree(tree_dict,root,tmp_nodes,None,my_tree)
    my_tree.show()

    #print(tree_dict)
    print(my_tree.depth())
    depth = my_tree.depth()
    add_balance(tree_dict,my_tree,my_tree.root,False,depth)
    #print(tree_dict)
    check_balance(tree_dict,my_tree,my_tree.root)
    #my_tree.show()
    #print("My Tree",tmp_nodes)
    #test()


def check_balance(tree_dict,my_tree,currentNode):
    balanced = True
    first_val = None
    current_val = None
    first_node = None
    current_node = None
    for node in my_tree.is_branch(currentNode):
        #print("Node",node,tree_dict[node]["total_weight"])
        current_val = tree_dict[node]["total_weight"]
        current_node = node
        print("c v", node, current_val)

        if first_val == None:
            first_val = current_val
            first_node = node
        if first_val != current_val:
            balanced = False

        #add_balance(tree_dict,my_tree,node,add,current_depth)
    print("Balanced: ", balanced, first_val, current_val)
    print("Adjust: ", first_val - current_val)
    print("Nodes", first_node, current_node)

def add_balance(tree_dict,my_tree,currentNode,add,current_depth):
    # check depth, then get nodes at each depth and add values up to parent
    current_depth = my_tree.depth(currentNode)
    if my_tree.depth() == current_depth: #Add values to Parent until reach root
        parent = my_tree.parent(currentNode).tag
        #print("Parent", parent)
        while(tree_dict[parent]) != None:
            tree_dict[parent]["total_weight"] = tree_dict[parent]["total_weight"] + tree_dict[currentNode]["weight"]
            if my_tree.parent(parent) is None:
                break
            else:
                parent = my_tree.parent(parent).tag

        add = True
        #add value to parent
    for node in my_tree.is_branch(currentNode):
        add_balance(tree_dict,my_tree,node,add,current_depth)
    #Move down until children are leave nodes...
    #See if children balance if so add children to node weight
    #Check next one and move up a level

class Weight(object):
        def __init__(self, weight, total_weight):
            self.weight = weight
            self.total_weight = total_weight



def check_weights(root,tmp_nodes):
    root_node = tmp_nodes[root]
    weight = int(root_node['weight'])

    print("Printing Child weights",root,root_node,weight)
    child_nodes = root_node['children']
    node_children_weight = 0
    for child in child_nodes:
        child_name = child.strip()
        print(child_name,tmp_nodes[child_name]['total_weight'])

def build_tree(tree_dict,root,tmp_nodes,parent,my_tree):
    root_node = tmp_nodes[root]
    weight = int(root_node['weight'])
    if (parent is None):
        my_tree.create_node(root,root,data=Weight(weight,weight))
        tree_dict[root] = {"weight":weight,"total_weight":weight,"parent":None}
    else:
        my_tree.create_node(root,root,parent=parent,data=Weight(weight,weight))
        tree_dict[root] = {"weight":weight,"total_weight":weight,"parent":parent}
        parent = jtree

        # Update parent weights
    print("ROOT",root,root_node,weight)
    child_nodes = root_node['children']
    node_children_weight = 0
    for child in child_nodes:
        child_name = child.strip()
        build_tree(tree_dict,child_name,tmp_nodes,root,my_tree)


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

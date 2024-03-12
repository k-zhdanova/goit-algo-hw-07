class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(node, key):
    if node is None:
        return Node(key)
    else:
        if key < node.val:
            node.left = insert(node.left, key)
        else:
            node.right = insert(node.right, key)
    return node

def findMaxValue(node):
    current = node
    # loop down to find the rightmost leaf
    while(current.right):
        current = current.right
    return current.val

def findMinValue(node):
    current = node
    # loop down to find the leftmost leaf
    while(current.left):
        current = current.left
    return current.val

def sumOfValues(node):
    if node is None:
        return 0
    return node.val + sumOfValues(node.left) + sumOfValues(node.right)

# Let's create a binary search tree
root = Node(10)
insert(root, 5)
insert(root, 1)
insert(root, 7)
insert(root, 40)
insert(root, 50)

max_value = findMaxValue(root)
print("The maximum value in the binary search tree is: ", max_value)

min_value = findMinValue(root)
print("The minimum value in the binary search tree is: ", min_value)

total_sum = sumOfValues(root)
print("The sum of all values in the binary search tree is: ", total_sum)

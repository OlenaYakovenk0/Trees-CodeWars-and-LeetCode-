class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

def pre_order(node):
    if not node:
        return []
    return [node.data] + pre_order(node.left) + pre_order(node.right)

def in_order(node):
    if not node:
        return []
    return in_order(node.left) + [node.data] + in_order(node.right)

def post_order(node):
    if not node:
        return []
    return post_order(node.left) + post_order(node.right) + [node.data]

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.left = b
a.right = c
c.left = d

print(pre_order(a))
print(in_order(a))
print(post_order(a))

# preOrder(a) should return ["A", "B", "C", "D"]
# inOrder(a) should return ["B", "A", "D", "C"]
# postOrder(a) should return ["B", "D", "C", "A"]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def deleteNode(self, root, key: int):
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            newnode = self.findmin(root.right)
            root.val = newnode.val
            root.right = self.deleteNode(root.right, newnode.val)
        return root

    def findmin(self, node):
        while node.left:
            node = node.left
        return node

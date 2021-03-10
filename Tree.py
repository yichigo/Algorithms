class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def addRow(node, depth, isLeft):
            if depth == d:
                newNode = TreeNode(v)
                if isLeft:
                    newNode.left = node
                else:
                    newNode.right = node
                return newNode
            
            if not node:
                return node
            
            node.left = addRow(node.left, depth + 1, 1)
            node.right = addRow(node.right, depth + 1, 0)
            return node
            
        return addRow(root, 1, 1)
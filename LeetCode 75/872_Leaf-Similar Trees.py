# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a1 = []
        a2 = []
        def traversal(node, a):
            if node.left == None and node.right == None:
                a.append(node.val)
            if node.left != None:
                traversal(node.left, a)
            if node.right != None:
                traversal(node.right, a)

        traversal(root1, a1)
        traversal(root2, a2)
        return a1 == a2
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traversal(node):
            if node != None:
                arr.append(node.val)
                if arr[-1] >= max(arr[:len(arr)]):
                    cnt[0] += 1

                traversal(node.left)
                traversal(node.right)
                arr.pop()
                
        arr = []
        cnt = [0]
        traversal(root)
        return cnt[0]

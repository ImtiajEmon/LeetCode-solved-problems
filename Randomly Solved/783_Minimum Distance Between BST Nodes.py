# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = []

        def dfs(node):
            arr.append(node.val)
            if node.left != None:
                dfs(node.left)
            if node.right != None:
                dfs(node.right)

        dfs(root)
        arr.sort()
        ans = 1e6

        for i in range(0, len(arr)-1):
            ans = min(ans, abs(arr[i] - arr[i+1]))

        return ans

        

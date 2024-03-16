# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        a = []
        def dfs(root):
            nonlocal ans
            if root == None:
                return

            a.append(root.val)
            dfs(root.left)
            dfs(root.right)

            sum = 0
            for i in range(len(a)-1, -1, -1):
                sum += a[i]
                if sum == targetSum:
                    ans += 1

            a.pop()

        dfs(root)
        return  ans

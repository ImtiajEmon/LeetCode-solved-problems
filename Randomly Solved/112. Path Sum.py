# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def path_sum(node, cur_sum):
            if not node:
                return False

            cur_sum += node.val
            # chech weather i am at leaf node or not
            if not node.left and not node.right:
                return cur_sum == targetSum

            return path_sum(node.left, cur_sum) or path_sum(node.right, cur_sum)

        return path_sum(root, 0)

        

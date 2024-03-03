# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        from queue import Queue

        q = Queue()
        q.put(root)
        level = 1
        ans = 0
        lsum = -1e6

        while not q.empty():
            cur_sum = 0
            cnt = q.qsize()

            while cnt:
                frnt = q.get()
                cur_sum += frnt.val

                if frnt.left:
                    q.put(frnt.left)
                if frnt.right:
                    q.put(frnt.right)

                cnt -= 1

            if cur_sum > lsum:
                lsum = cur_sum
                ans = level

            level += 1

        return ans

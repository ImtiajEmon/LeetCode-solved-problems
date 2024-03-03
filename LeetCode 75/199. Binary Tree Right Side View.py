# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from queue import Queue
        if not root:
            return 

        q = Queue()
        q.put(root)
        ans = []

        while not q.empty():
            arr = []
            cnt = q.qsize()

            while cnt:
                frnt = q.get()
                arr.append(frnt.val)
                if frnt.left:
                    q.put(frnt.left)
                if frnt.right:
                    q.put(frnt.right)
                cnt -= 1

            if arr:
                ans.append(arr[-1])

        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        from queue import Queue
        q = Queue()
        q.put(root)

        while not q.empty():
            frnt = q.get()

            if frnt != None:
                q.put(frnt.left)
                q.put(frnt.right)
            else:
                while not q.empty():
                    frnt = q.get()
                    if frnt != None:
                        return False
        return True
        

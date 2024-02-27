# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        leng = 0
        it = head

        while it != None:
            leng += 1
            it = it.next

        half = leng//2
        temp = head
        arr = []
        i = 0
        while i < half:
            arr.append(temp.val)
            temp = temp.next
            i += 1

        it = -1
        ans = -100
        while temp != None:
            ans = max(ans, arr[it] + temp.val)
            it -= 1
            temp = temp.next

        return ans

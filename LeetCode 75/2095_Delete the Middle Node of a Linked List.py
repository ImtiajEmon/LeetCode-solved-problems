# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        leng = 0
        temp = head

        while temp != None:
            leng += 1
            temp = temp.next

        mid = leng // 2

        i = 0
        temp = head
        while i < mid-1:
            temp = temp.next
            i += 1
        
        if leng == 1:
            head = None
        elif leng == 2:
            temp.next = None
        else:
            temp.next = temp.next.next

        return head

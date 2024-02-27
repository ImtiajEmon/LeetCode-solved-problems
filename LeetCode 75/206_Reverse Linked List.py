# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        iterator = head
        head = None

        while iterator != None:
            temp = iterator.next
            iterator.next = head
            head = iterator
            iterator = temp

        return head
        

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      head = None
      temp  = None
      carry = 0

      while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        res = val1 + val2 + carry
        carry = res // 10
        res = res % 10

        node = ListNode(res)

        if head == None:
          head = node

        if temp != None:
          temp.next = node

        temp = node

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

      return head

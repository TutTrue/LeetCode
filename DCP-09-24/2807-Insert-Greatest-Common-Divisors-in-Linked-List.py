# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        def GCD(a, b):
            if a < b:
                a, b = b, a
            if (b == 0):
                return a
            return GCD(b, a%b)
        c, n = head, head.next
        while n:
            c.next = ListNode(GCD(c.val, n.val), n)
            c = n
            n = c.next
        return head
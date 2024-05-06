# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = ListNode(0)
        s = []
        cur = head
        while cur:
            while s and cur.val > s[-1].val:
                s.pop()
            s.append(cur)
            cur = cur.next
        cur = t
        for i in s:
            cur.next = i
            cur =cur.next
        return t.next

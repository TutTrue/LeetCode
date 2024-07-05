# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head.next.next:
            return [-1, -1]

        def increment(li):
            for i in range(len(li)):
                li[i] += 1

        critical = []
        idx = 1
        p, c, n = head, head.next, head.next.next

        while n:
            s = 0
            if (c.val > p.val and c.val > n.val) or (c.val < p.val and c.val < n.val):
                critical.append(idx)
            idx+=1
            p = p.next
            c = c.next
            n = n.next
        if len(critical) < 2:
            return [-1, -1]
        mi = float('inf')
        for i in range(1, len(critical)):
            mi = min(mi, critical[i] - critical[i-1])
        return [mi, critical[-1] - critical[0]]

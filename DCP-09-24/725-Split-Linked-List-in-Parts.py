# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        l = 0
        while cur:
            l+=1
            cur = cur.next

        cur = head
        prev = None
        res = [None] * k
        i = 0
        if l < k:
            while cur:
                res[i] = cur
                cur = cur.next
                res[i].next = None
                i+=1
        else:
            mod = l % k
            k = l // k

            for i in range(mod):
                res[i] = cur
                for _ in range(k):
                    cur = cur.next
                prev = cur
                cur = cur.next
                prev.next = None
            i = mod
            while cur:
                res[i] = cur
                i+=1
                for _ in range(k - 1):
                    cur = cur.next
                prev = cur
                cur = cur.next
                prev.next = None

        return res

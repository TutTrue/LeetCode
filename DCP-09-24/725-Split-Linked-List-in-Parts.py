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
        res = [None] * k
        mod = l % k if k < l else 0
        k = l // k if k < l else 0
        i = 0
        def append_split(cur, k, i):
            res[i] = cur
            for _ in range(k):
                cur = cur.next
            prev = cur
            cur = cur.next
            prev.next = None
            return cur
        for i in range(mod):
            cur = append_split(cur, k, i)
        i = mod
        while cur:
            cur = append_split(cur, k - 1, i)
            i+=1

        return res

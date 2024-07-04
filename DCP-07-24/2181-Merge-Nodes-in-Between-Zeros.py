# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        idx = head # the index that will be modified
        prev_idx = None
        while cur:
            s = 0
            while cur.val != 0:
                s+=cur.val
                cur = cur.next
            idx.val = s
            prev_idx = idx
            idx = idx.next
            cur = cur.next
        prev_idx.next=None
        return head.next
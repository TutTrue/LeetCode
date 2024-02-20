# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        def reverseList(head):
            tmp = head
            cur = None
            while tmp:
                head = head.next
                tmp.next = cur
                cur = tmp
                tmp = head
            return cur
        
        i = 0
        tmp = head
        cur = head
        h = head
        prev_list = None
        while cur:
            cur = tmp
            while cur and i < k - 1:
                i+=1
                cur = cur.next
            if not cur:
                return head
            tmp =cur.next
            cur.next = None
            if prev_list:
                prev_list.next = None
            cur = reverseList(h)
            if not prev_list:
                head = cur
            else:
                prev_list.next = cur
            h.next = tmp
            prev_list = h
            h = tmp
            i=0
        return head
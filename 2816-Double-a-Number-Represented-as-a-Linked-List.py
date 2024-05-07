# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = 0
        def rec(cur=head):
            nonlocal s
            if not cur:
                s*=2
                return
            s*=10
            s+=cur.val
            rec(cur.next)
            cur.val = s%10
            s=s//10
        rec()
        while s != 0:
            tmp = ListNode(s%10)
            tmp.next = head
            head = tmp
            s=2//10
        return head
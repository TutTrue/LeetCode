# 82. Remove Duplicates from Sorted List II

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        c = head
        s = set()
        while c.next:
            if c.val == c.next.val:
                s.add(c.val)
            c = c.next
        while head and head.val in s:
            head = head.next
        if not head or not head.next:
            return head
        c = head
        n = c.next
        while n:
            if n.val in s:
                n = n.next
            else:
                c.next = n
                c = n
                n = n.next
        c.next = n
        return head

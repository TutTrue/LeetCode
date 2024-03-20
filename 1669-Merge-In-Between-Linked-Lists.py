# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l = h = list1
        for i in range(a - 1):
            l = l.next
        h = l
        for i in range(b - a + 2):
            h = h.next
        l.next = list2
        cur = list2
        while cur.next:
            cur = cur.next
        cur.next = h
        return list1
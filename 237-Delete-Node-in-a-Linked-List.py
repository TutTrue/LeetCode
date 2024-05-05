# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        \\\
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        \\\
        cur = node
        while cur:
            cur.val = cur.next.val
            if not cur.next.next:
                cur.next = None
            cur = cur.next
        
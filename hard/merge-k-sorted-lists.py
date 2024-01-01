# 23. Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = None
        for i in lists:
            head = self.mergeTwoLists(head, i)
        return head

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
    
        head = None
        if list1.val < list2.val:
            head = list1
            cur1 = list1.next
            cur2 = list2
        else:
            head = list2
            cur1 = list1
            cur2 = list2.next
    
        prev = head
    
        while cur1 and cur2:
            if cur1.val < cur2.val:
                prev.next = cur1
                prev = cur1
                cur1 = cur1.next
            else:
                prev.next = cur2
                prev = cur2
                cur2 = cur2.next
    
        if cur1:
            prev.next = cur1
        else:
            prev.next = cur2
    
        return head

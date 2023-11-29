# 160. Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dic = set()
        cura = headA
        curb = headB

        while cura or curb:
            if cura:
                if cura in dic:
                    return cura
                else:
                    dic.add(cura)
                    cura = cura.next
            if curb:
                if curb in dic:
                    return curb
                else:
                    dic.add(curb)
                    curb = curb.next

        return None

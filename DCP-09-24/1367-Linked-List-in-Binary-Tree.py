# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.dfs(root, head): return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def dfs(self, root, head):
        if not head:
            return True
        if not root:
            return False
        if root.val != head.val:
            return False
        return self.dfs(root.left, head.next) or self.dfs(root.right, head.next)

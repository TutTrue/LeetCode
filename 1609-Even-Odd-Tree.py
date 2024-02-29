# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        odd = deque([root])
        even = deque()
        while even or odd:
            prev = None
            while odd:
                temp = odd.popleft()
                if temp.val % 2 == 0 or (prev and temp.val <= prev.val):
                    return False
                if temp.left:
                    even.append(temp.left)
                if temp.right:
                    even.append(temp.right)
                prev = temp
            prev = None
            while even:
                temp = even.popleft()
                if temp.val % 2 != 0 or (prev and temp.val >= prev.val):
                    return False
                if temp.left:
                    odd.append(temp.left)
                if temp.right:
                    odd.append(temp.right)
                prev = temp
        return True
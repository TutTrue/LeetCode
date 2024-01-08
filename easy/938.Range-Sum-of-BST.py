# 938. Range Sum of BST

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        li = [root]
        s=0
        while li:
            t = li.pop()
            if t.left:
                li.append(t.left)
            if t.right:
                li.append(t.right)
            s+=t.val if t.val >= low and t.val <= high else 0
        return s

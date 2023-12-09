# 94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        li = []
        self.traverse(root, li)
        return li
    def traverse(self, root, li):
        if not root:
            return
        self.traverse(root.left, li)
        li.append(root.val)
        self.traverse(root.right, li)

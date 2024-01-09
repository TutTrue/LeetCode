# 872. Leaf-Similar Trees

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def inorder(tree, leaf=[]):
            if not tree:
                return
            inorder(tree.left, leaf)
            if not tree.left and not tree.right: # append if leaf
                leaf.append(tree.val)
            inorder(tree.right, leaf)
            return leaf

        return inorder(root1, []) == inorder(root2, [])

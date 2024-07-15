# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        dic = {}
        s = set()
        for p, n, isleft in descriptions:
            if n not in dic:
                dic[n] = TreeNode(n)
            if p not in dic:
                dic[p] = TreeNode(p)

            if isleft:
                dic[p].left = dic[n]
            else:
                dic[p].right = dic[n]
            s.add(n)
        for p, n, isleft in descriptions:
            if p not in s:
                return dic[p]
        return None
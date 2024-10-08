"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        def rec(node=root):
            if not node:
                return
            for n in node.children:
                rec(n)
            res.append(node.val)
        rec()
        return res
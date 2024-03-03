"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def bfs(node, level):
            if not node:
                return level
            m = level + 1
            for ch in node.children:
                m = max(m, bfs(ch, level+1))
            return m
        return bfs(root, 0)
        
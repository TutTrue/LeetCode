\\\
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
\\\

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dic = {None: None}
        dic[head] = Node(head.val)
        cur = head
        while cur.next:
            dic[cur.next] = Node(cur.next.val)
            dic[cur].next = dic[cur.next]
            cur = cur.next
        cur = head
        while cur:
            dic[cur].random = dic[cur.random]
            cur = cur.next

        return dic[head]
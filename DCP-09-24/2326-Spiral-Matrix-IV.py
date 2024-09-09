# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        grid = [[-1] * n for _ in range(m)]
        current = head
        top, left, right, bottom = 0, 0, n-1, m-1

        while current and left <= right and top <= bottom:
            for i in range(left, right+1):
                if current:
                    grid[top][i] = current.val
                    current = current.next
            top += 1

            for i in range(top, bottom+1):
                if current:
                    grid[i][right] = current.val
                    current = current.next
            right -= 1

            if left <= right:
                for i in range(right, left-1, -1):
                    if current:
                        grid[bottom][i] = current.val
                        current = current.next
            bottom -= 1

            if top <= bottom:
                for i in range(bottom, top-1, -1):
                    if current:
                        grid[i][left] = current.val
                        current = current.next
            left += 1
            
        return grid
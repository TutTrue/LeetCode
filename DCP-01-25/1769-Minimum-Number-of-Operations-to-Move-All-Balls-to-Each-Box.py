class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)

        moves = balls = 0
        for i in range(len(boxes)):
            res[i] = moves + balls

            moves += balls
            balls += int(boxes[i])

        moves = balls = 0
        for i in range(len(boxes) -1 , -1 , -1):
            res[i] += moves + balls

            moves += balls
            balls += int(boxes[i])

        return res
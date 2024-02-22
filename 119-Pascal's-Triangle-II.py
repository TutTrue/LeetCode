class Solution:
    def getRow(self, numRows: int) -> List[int]:
        if numRows < 0:
            return []
        if numRows == 0:
            return [1]
        res = [[1], [1,1]]
        for i in range(numRows):
            li = [1]
            for j in range(i):
                li.append(res[1][j]+res[1][j+1])
            li.append(1)
            res.append(li)
            res.pop(0)
        return res[-1]
        
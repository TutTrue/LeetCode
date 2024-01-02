# 2610. Convert an Array Into a 2D Array With Conditions

class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        freq = defaultdict(int)
        res = []
        for i in nums:
            freq[i] +=1
        while True:
            li = []
            for k, v in freq.items():
                if v > 0:
                    li.append(k)
                    freq[k]-=1
            if not li:
                break
            res.append(li)
        return res

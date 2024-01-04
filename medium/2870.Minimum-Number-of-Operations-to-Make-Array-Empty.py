# 2870. Minimum Number of Operations to Make Array Empty

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = defaultdict(int)
        counter = 0
        for i in nums:
            dic[i]+=1
        for v in dic.values():
            if v == 1:
                return -1
            counter +=(v - 1) // 3 + 1

        return counter

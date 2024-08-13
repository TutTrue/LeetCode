class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def rec(i=0, li=[], cur_sum=0):
            if cur_sum == target:
                res.append(li[:])
                return
            if i == len(candidates) or cur_sum > target:
                return
            
            li.append(candidates[i])
            rec(i+1, li, cur_sum+candidates[i])

            li.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
                
            rec(i+1, li, cur_sum)

        rec()
        return res
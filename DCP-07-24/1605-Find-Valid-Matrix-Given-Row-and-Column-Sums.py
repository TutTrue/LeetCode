class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if m*k>n:
            return -1
        left=1
        right=max(bloomDay)
        while left<right:
            mid=(left+right)//2
            run=0
            count=0
            for day in bloomDay:
                
                if day>mid:
                    run=0 
                else:
                    run+=1
                if run>=k:
                    run=0
                    count+=1
                    if count==m:
                        break
            if count==m:
                right=mid
            else:
                left=mid+1
        return left         
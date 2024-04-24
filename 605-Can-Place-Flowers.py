class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = n
        r = 0
        c=1
        while r < len(flowerbed):
            if flowerbed[r] == 1:
                c=0
            else:
                c+=1
                if c == 3:
                    m-=1
                    c=0
                    r-=1
            r+=1
        if c == 2:
            m-=1
        return m <= 0
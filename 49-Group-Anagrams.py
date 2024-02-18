class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        li = []
        counter = 0
        for st in strs:
            if str(sorted(st)) in dic:
                li[dic[str(sorted(st))]].append(st)
            else:
                dic[str(sorted(st))] = counter
                counter+=1
                li.append([st])
        return li
        
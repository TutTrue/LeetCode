class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        index_map = {p: i for i, p in enumerate(positions)}
        stack = []

        for p in sorted(positions):
            i = index_map[p]
            if directions[i] == "R":
                stack.append(i)
            else:
                while stack and healths[i]:
                    j = stack.pop()
                    if healths[i] > healths[j]:
                        healths[j] = 0
                        healths[i] -= 1
                    elif healths[i] < healths[j]:
                        healths[i] = 0
                        healths[j] -= 1
                        stack.append(j)
                    else:
                        healths[i] = healths[j] = 0
        return [h for h in healths if h > 0]

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rotated = [list(x) for x in zip(*box[::-1])]

        for i in range(len(rotated) - 2, -1, -1):
            for j in range(len(rotated[i])):
                if rotated[i][j] == '#':
                    a = i+1
                    while a < len(rotated) and rotated[a][j] == '.':
                        rotated[a-1][j] = '.'
                        rotated[a][j] = '#'
                        a+=1

        return rotated
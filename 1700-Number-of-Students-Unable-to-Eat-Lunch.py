class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st = deque(students)
        sdi = 0
        while st:
            i = 0
            while st[0] != sandwiches[sdi] and i < len(st):
                st.rotate(-1)
                i+=1
            if i == len(st):
                return len(st)
            else:
                st.popleft()
            sdi+=1
        return 0
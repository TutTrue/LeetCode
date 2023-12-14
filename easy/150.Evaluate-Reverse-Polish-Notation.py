# 150. Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token == "+":
                st.append(int(st.pop()) + int(st.pop()))
            elif token == "*":
                st.append(int(st.pop()) * int(st.pop()))
            elif token == "-":
                num1 = int(st.pop())
                num2 = int(st.pop())
                st.append(num2-num1)
            elif token == "/":
                num1 = int(st.pop())
                num2 = int(st.pop())
                st.append(num2/num1)
            else:
                st.append(token)

        return int(st.pop())

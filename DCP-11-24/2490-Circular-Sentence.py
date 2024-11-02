class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if len(sentence) == 1:
            return True
        if sentence[0] != sentence[-1]:
            return False

        sentence = sentence.split()
        last_char = sentence[0][-1]
        for i in range(1, len(sentence)):
            if sentence[i][0] != last_char:
                return False
            last_char = sentence[i][-1]
        return True
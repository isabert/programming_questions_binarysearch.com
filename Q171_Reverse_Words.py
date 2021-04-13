class Solution:
    def solve(self, sentence):
        word = []
        start = 0

        for i in range(len(sentence)):
            if sentence[i] == " ":
                word.append(sentence[start:i])
                start = i + 1
        word.append(sentence[start:len(sentence)])
        res = ""

        for i in range(len(word) - 1, -1, -1):
            res += word[i]
            if (i != 0):
                res += " "

        return res
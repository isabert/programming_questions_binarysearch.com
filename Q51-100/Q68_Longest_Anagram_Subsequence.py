class Solution:
    def solve(self, a, b):
        count_a = [0]*26
        count_b = [0]*26

        for c in a:
            count_a[ord(c)-ord('a')]+=1

        for c in b:
            count_b[ord(c)-ord('a')]+=1

        anagram = 0
        for i in range(26):
            anagram+=min(count_a[i], count_b[i])

        return anagram
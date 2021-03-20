class Solution:
    def solve(self, pattern, s):
        n = len(s)
        m = len(pattern)
        pattern = " " + pattern
        s = " " + s

        mat = [[False] * (m + 1) for i in range(n + 1)]

        mat[0][0] = True;

        # because "" match with "a*"
        for i in range(1, m + 1):
            if (pattern[i] == '*'): mat[0][i] = mat[0][i - 2];

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if (s[i] == pattern[j] or pattern[j] == '.'):
                    mat[i][j] = mat[i - 1][j - 1];
                elif (pattern[j] == '*'):
                    mat[i][j] = mat[i][j - 2];
                    if (pattern[j - 1] == '.' or s[i] == pattern[j - 1]): mat[i][j] = mat[i][j] or mat[i - 1][j];

        return mat[n][m];

    def solve2(self, pattern, s):
        @lru_cache(None)
        def dp(pattern=pattern, s=s):
            if not pattern or not s:
                # if any of these is empty, we check if both are empty or
                # the pattern is of the form: 'x*' where x can be anything
                return (not pattern and not s) or (len(pattern) == 2 and pattern[-1] == "*")

            if pattern[0] == ".":
                # if we come across '.*' we try to consider matching 0 to
                # the remaining length of s number of characters and recurse
                # on the remaining characters in s
                if len(pattern) > 1 and pattern[1] == "*":
                    return any(dp(pattern[2:], s[k:]) for k in range(len(s) + 1))

                # this means that
                return dp(pattern[1:], s[1:])

            # if the pattern starts with 'x*', we first check if we can consider
            # 0 characters of the current character in pattern
            # we do this separately because of the next condition
            if len(pattern) > 1 and pattern[1] == "*" and dp(pattern[2:], s):
                return True

            # if current character doesn't match, just return False
            if pattern[0] != s[0]:
                return False

            # if the pattern starts with 'x*' where x can be any character,
            # we check all counts of x as long as it matches in the string s
            # and recurse on the remaining characters in s
            if len(pattern) > 1 and pattern[1] == "*":
                current_char = pattern[0]
                j = 0
                while j < len(s) and current_char == s[j]:
                    if dp(pattern[2:], s[j + 1:]):
                        return True
                    j += 1
                return False

            # if nothing from the above applies, it means it's just
            # normal character comparison and pattern[0]==s[0] so we just start
            # with the next characters in each string
            return dp(pattern[1:], s[1:])

        return dp()

pattern0 = 'a'
string0 = 'aa'
sol0 = False

pattern1 ="l.*ing"
string1 = "look interesting"
sol1 = True

pattern2 = "pirat*e"
string2 = "pirate"
sol2 = True

pattern3 = "girafe"
string3 = "giraffe"
sol3 = False

pattern4 = "g.*rra.*fe"
string4  ="giiraaffe"
sol4 = False

pattern5 = "g*r*fe"
string5  ="fe"
sol5 = True

solution = Solution()
print(solution.solve(pattern = pattern0, s =string0))
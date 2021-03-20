class Solution:
    def solve(self, n, friends):
        has_friend = [False] * n
        for friend_group in friends:
            has_friend[friend_group[0]] = True
            has_friend[friend_group[1]] = True

        for person in has_friend:
            if (person == False):
                return False

        return True
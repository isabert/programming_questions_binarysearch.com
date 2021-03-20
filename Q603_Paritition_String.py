class Solution:
    def solve(self, s):
        if (s == ''): return []
        appearance = {}
        for i in range(len(s)):
            c = s[i]
            if (appearance.get(c) != None):
                appearance[c]['last'] = i
            else:
                appearance[c] = {'first': i, 'last': i}

        l = -1
        u = -1
        result = []

        # python dict appear by the order the element is first added
        # otherwise, appearance should be shorted by first

        def in_range(l, u, index):
            if (l <= index and index <= u):
                return True
            return False

        for k in appearance:
            k_l = appearance[k]['first']
            k_u = appearance[k]['last']
            if (l == -1 and u == -1):
                l = k_l
                u = k_u
                continue
            if (in_range(l, u, k_l) or in_range(l, u, k_u)):
                l = min(l, k_l)
                u = max(u, k_u)
            else:
                result.append(u - l + 1)
                l = k_l
                u = k_u

        result.append(u - l + 1)
        return result
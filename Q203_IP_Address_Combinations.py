class Solution:
    def solve(self, ip):
        sol = []
        n = len(ip)

        # insertion is an array, means there is a comma after
        def check_validity(insertion):
            start = 0
            for i in range(4):
                if (i == 3):
                    end = len(ip)
                else:
                    ins = insertion[i]
                    end = ins + 1
                qtr_ip = ip[start:end]
                start = end
                if (qtr_ip == None or int(qtr_ip) > 255 or (qtr_ip[0] == '0' and int(qtr_ip) != 0)):
                    return False

            return True

        def rec(insertion, i):
            if (i == n):
                return
            if (len(insertion) == 3):
                if (check_validity(insertion)):
                    sol.append(insertion)
                return
            insertion_apd = copy.deepcopy(insertion)
            insertion_apd.append(i)
            rec(insertion_apd, i + 1)
            rec(insertion, i + 1)

        rec([], 0)
        res = []
        for insertion in sol:
            ip_copy = copy.deepcopy(ip)
            for i in range(3 - 1, -1, -1):
                ip_copy = ip_copy[:(insertion[i] + 1)] + '.' + ip_copy[(insertion[i] + 1):]
            res.append(ip_copy)

        return res


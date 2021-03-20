class Solution:
    def solve(self, graph):
        # there are at most 25 nodes
        # Q4 cannot be cracked with any naive method if it's highly connected.

        # we shall use bipartite
        # 1 and 2 are the two colors
        # the default is None
        n = len(graph)
        if (n == 0): return True
        nodes = [None] * n

        def check_bipartite(color, i):

            if (nodes[i] == None):
                # first time visit
                nodes[i] = color
                flag = None
                color_bar = (color + 1) % 2
                for n in graph[i]:
                    if (flag == None):
                        flag = check_bipartite(color_bar, n)
                    else:
                        flag = flag and check_bipartite(color_bar, n)
                return flag
            elif (nodes[i] != color):
                # already visited, odd loop
                return False
            else:
                # already visited, even loop
                return True

        for i in range(n):
            b = False
            if (nodes[i] == None):
                print(i)
                print(nodes)
                b = check_bipartite(1, i) == False
                if (b == True):
                    return True
        # if b is false, it means check_bipartite's either none(1 node) of True
        return False



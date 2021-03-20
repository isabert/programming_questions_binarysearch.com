#from tutorial
import heapq
class Solution:
    def solve(self, lists):
        min_heap = []

        for i in range(len(lists)):
            if len(lists[i]) > 0:
                heapq.heappush(min_heap, (lists[i][0], i, 0))

        res = []

        while len(min_heap) > 0:
            a, i, j = heapq.heappop(min_heap)

            if j + 1 < len(lists[i]):
                heapq.heappush(min_heap, (lists[i][j + 1], i, j + 1))

            res.append(a)

        return res


#assume n is the number of rows and m is the longest list in column:

#method 1:
#tutorial: putting the first element of list in heap
#time complexity: O(m*n*log(n)) need m*n retrivals, each retrival is log(n)
#space complexity:O(n)

#method 2: push all elements into a array, then sort the array
#time complexity: O(m*n*log(mn)): quick sort takes o(a*log(a)) time to sort for element of length a
#space complexity:O(m*n)

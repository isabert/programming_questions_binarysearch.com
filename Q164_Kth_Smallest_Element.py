import random
import heapq
#sol1 and sol4 are the parts that are the most important
#sol3 and sol4 has 2 diffrent partition methods

class Solution:
    def solve(self, nums, k):
        return self.sol4(nums, k)

    def sol1(self, nums, k):
        # method 1:use max heap for elements 0 to k-1 and keep adding in elements
        # time complexity: O(k*log(k)+(n-k)*log(k)) = O(n*log(k))
        # 1.1uses heapq
        heap = []
        for i in range(len(nums)):
            num = -1 * nums[i]
            heapq.heappush(heap, num);
            if (i > k):
                heapq.heappop(heap);
        return -1 * heapq.heappop(heap)

    def sol2(self, nums, k):
        # method 1:use max heap for elements 0 to k-1 and keep adding in elements
        # 1.2write my own heap
        # time complexity: O(k*log(k)+(n-k)*log(k)) = O(n*log(k))
        # runtime exceeded??
        heap = [0]

        def fix_up(heap, i):
            while (i > 1):
                if (heap[i] > heap[i // 2]):
                    heap[i], heap[i // 2] = heap[i // 2], heap[i]
                    i //= 2
                else:
                    break

        def fix_down(heap, i):
            if (i == 0): return
            while (i * 2 < len(heap)):
                nxt = i * 2
                if (nxt + 1 < len(heap) and heap[nxt + 1] > heap[nxt]):
                    nxt += 1
                if (heap[i] < heap[nxt]):
                    heap[i], heap[nxt] = heap[nxt], heap[i]
                    i = nxt
                else:
                    break;

        for i in range(len(nums)):
            num = nums[i]
            if (i > k):
                if (heap[1] > num):
                    heap[1] = num
                else:
                    heap.append(num)
                    fix_up(heap, len(heap) - 1);
                    heap[len(heap) - 1], heap[1] = heap[1], heap[len(heap) - 1]
                    heap.pop(len(heap) - 1)
                fix_down(heap, 1)
            else:
                heap.append(num)
                fix_up(heap, len(heap) - 1);

        return heap[1]

    def sol3(self, nums, k):
        # method 2:
        # uses quickselect: quicksort, except we only "sort" 1 side of the pivot
        # we quicksort stops the moment the k_th smallest element is the pivot
        # has an average time complexity of O(N), worse case being O(N^2)

        # randomly select pivot to aim for complexity O(N)

        rand_pivot = int(random.randint(0, len(nums) - 1))
        nums[rand_pivot], nums[len(nums) - 1] = nums[len(nums) - 1], nums[rand_pivot]
        # l and r are boundaries
        l = 0
        r = len(nums)-1
        i = l-1
        j = r
        pivot = nums[r]
        while (True):
            while ( i < r):
                i += 1
                if(nums[i]>pivot):break;
            while (j > l):
                j -= 1
                if(nums[j]<pivot):break;

            if (i < j ):
                nums[i], nums[j] = nums[j], nums[i]
            else:
                # the current range is partitioned into 2
                print(pivot)
                print(i)
                print(j)
                print(nums)
                nums[i], nums[r] = nums[r], nums[i]
                print(nums)
                if (k > i):
                    l = i+1
                    i = l-1
                    j = r
                elif (k < i):
                    r = i-1
                    i = l-1
                    j = r
                else:  # k==i
                    return nums[i]
                if(l>r):print('{},{}'.format(l,r))
                rand_pivot = int(random.randint(l, r))
                nums[rand_pivot], nums[r] = nums[r], nums[rand_pivot]
                pivot = nums[r]

    def partition(self, nums, l, r):
        i = l - 1
        pivot = nums[r]
        for j in range(l, r):
            if (nums[j] < pivot):
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]

        return i + 1

    def sol4(self, nums, k):
        l = 0
        r = len(nums) - 1
        while (l <= r):
            pivot_ind = self.partition(nums, l, r)
            if (pivot_ind < k):
                l = pivot_ind + 1
            elif (pivot_ind > k):
                r = pivot_ind - 1
            else:
                return nums[pivot_ind]


s = Solution()
# nums = [5, 3, 8, 2, 0]
# k = 2

nums = [1, 0]
k = 0
print(s.solve(nums,k))
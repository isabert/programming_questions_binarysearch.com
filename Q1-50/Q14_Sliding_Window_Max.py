import heapq
class Solution:
    def solve_dict(self, nums, k):
        # uses dictionary
        # space: O(N)
        # time: O(KN)
        def get_max(l, r):
            mx_ind = l
            for i in range(l, r + 1):
                if (nums[i] > nums[mx_ind]):
                    mx_ind = i
            return mx_ind, nums[mx_ind]

        if (k == 1):
            return nums

        m_ind, m_val = 0, 0
        res = []
        for i in range(k - 1, len(nums)):
            if (i == k - 1):
                m_ind, m_val = get_max(0, k - 1)
            if (nums[i] > m_val):
                m_ind = i
                m_val = nums[i]
            if (m_ind <= i - k):
                m_ind, m_val = get_max(i - (k - 1), i)

            res.append(m_val)

        return res

    def solve_custome_heap(self, nums, k):
        if (k == 1):
            return nums
        heap = [0]  # heap is 1 indexed

        def fix_up(i):
            while (i > 1):
                if (heap[i] > heap[i // 2]):
                    heap[i], heap[i // 2] = heap[i // 2], heap[i]
                    i //= 2
                else:
                    break;

        def fix_down(i):
            while (i * 2 < len(heap)):
                j = i * 2
                if (j + 1 < len(heap) and heap[j + 1] > heap[j]):
                    j = j + 1
                if (heap[j] > heap[i]):
                    heap[i], heap[j] = heap[j], heap[i]
                    i = j
                else:
                    break

        res = []
        last_appeared = {}
        for i in range(len(nums)):
            n = nums[i]
            heap.append(n)
            last_appeared[n] = i
            fix_up(len(heap) - 1)
            if (len(heap) > k):
                while (last_appeared[heap[1]] < (i - k + 1)):
                    heap[1], heap[len(heap) - 1] = heap[len(heap) - 1], heap[1]
                    heap.pop(len(heap) - 1)
                    fix_down(1)
                res.append(heap[1])

        return res

    def solve_system_heap(self, nums, k):
        if(k==1):
            return nums
        #in heapq, the smallest index is actually 0
        heap = []
        res = []
        last_appeared = {}
        for i in range(len(nums)):
            n = nums[i]
            heapq.heappush(heap,-1*n)
            last_appeared[n]=i
            if(len(heap)>=k):
                while(last_appeared[heap[0]*-1]<(i-k+1)):
                    heapq.heappop(heap)
                res.append(-1*heap[0])

        return res

    def solve_monoqueue(self, nums, k):
        if (k == 1):
            return nums
        # this method uses monoqueue !!!!
        # time O(N)
        # space O(N)

        # to impliment the monoqueue in python, we shall uses deque(double queue)
        # monoqueue stores index have strickly decreasing values

        dq = []
        res = []
        for i in range(len(nums)):
            while (len(dq)):
                ind = dq[0]
                if (ind <= i - k):
                    dq.pop(0)
                else:
                    break
            while (len(dq)):
                ind = dq[len(dq) - 1]
                if (nums[i] > nums[ind]):
                    dq.pop(len(dq) - 1)
                else:
                    break

            dq.append(i)
            if (i >= k - 1):
                res.append(nums[dq[0]])
        return res
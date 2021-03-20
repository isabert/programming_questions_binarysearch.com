class Solution:
    def solve(self, nums, target):
        # we will use a INCREAING monoqueue for this problem
        # f=presum : count the presum of the first X numbers
        # Lemma: Let (i, j) be some ordered pair that minimizes j-i and satisfies f(j)−f(i)≥target. It must be the case that for all k in [i+1,j−1], f(k)>f(i).
        # Proof: Note that if f(k)≤f(i) , then we can replace i with k to get a strictly shorter subarray.

        # based on the editorial of @xiaowuc1
        # int solve(vector<int>& nums, int target) {
        #     int ans = 1e9;
        #     deque<pair<int, int>> q;
        #     q.emplace_back(0, 0);
        #     int curr = 0;
        #     for (int i = 0; i < nums.size(); i++) {
        #         curr += nums[i];
        #         while (q.size() && curr - q.front().first >= target) {
        #             ans = min(ans, i + 1 - q.front().second);
        #             q.pop_front();
        #         }
        #         while (q.size() && q.back().first >= curr) q.pop_back();
        #         q.emplace_back(curr, i + 1);
        #     }
        #     if (ans == 1e9) ans = -1;
        #     return ans;
        # }
        if (nums == []):
            return -1
        if (target == 0):
            for n in nums:
                if n >= 0:
                    return 1
            return -1

        cur_prefix = 0
        # deque contains pairs:(prefix_sum of first i numbers on the list,i)
        deque = [(0, 0)]
        res = None
        for i in range(len(nums)):
            cur_prefix += nums[i]
            while (len(deque)):
                element = deque[0]
                if (abs(element[0] - cur_prefix) >= target):
                    if (res == None or i - element[1] + 1 < res):
                        res = i - element[1] + 1
                    deque.pop(0)
                else:
                    break

            while (len(deque)):
                element = deque[len(deque) - 1]
                if (element[0] >= cur_prefix):
                    deque.pop(len(deque) - 1)
                else:
                    break
            deque.append((cur_prefix, i + 1))

        return res if res != None else -1
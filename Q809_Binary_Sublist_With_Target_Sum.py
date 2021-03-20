class Solution:
    def solve_myown(self, nums, target):
        #insight from @themast3r:
        #Use hash map and prefix sum. Maitaintain a running prefix sum and store the frequency of a sum as you encounter it in a map.
        #Say your current prefix sum is S and because you want the subarray sum to be target, you need number of prefix sums with count S - target
        #hash map gives you the count of some prefix sum x. Let's say your current prefix sum is S, then to get a subarray sum of target you need to substract a prefix
        #sum of S - target from it. So if have the count of number of time the prefix sum S - target has occured you can add it to your answer

        #the reason this is different than normal 2 pointers problem is because when sum ==target, should you increment the tail count or not and the answer is depend of the case:
        #here is an example where increasing the tail pointer would help:  nums = [1, 0, 1, 1]    target = 2
        #here is an example where increasing the tail pointer would not help: nums = [1,0]        targer = 1
        if(nums==[]): return 0
        count = {}
        prefix_sum = 0
        sol = 0
        for n in nums:
            prefix_sum +=n
            if(count.get(prefix_sum)==None):
                count[prefix_sum]=1
            else:
                count[prefix_sum]+=1

        if(target!=0):
            for c in count:
                if(c-target>=0 and count.get(c-target)!=None):
                    sol+=(count[c]*count[c-target])
                if(c-target==0):
                    sol+=count[c]
        else:
            for c in count:
                zero_count = 0
                if(count[c]>1 and c!=0):
                    zero_count=count[c]-1
                elif(c==0 and count[c]!=None):
                    zero_count = count[c]

                if(zero_count==1):
                    sol+=1
                elif(zero_count>1):
                    sol+=(1+zero_count)*zero_count//2

        return sol

    def solve(self, nums, target):
        # insight from @themast3r, @sidhhant24:
        '''
    int solve(vector<int>& nums, int target) {
        unordered_map<int, int> arr;
        arr[0] = 1;
        int ans = 0, sum = 0;
        for (auto t : nums) {
            sum += t;
            ans += arr[sum - target];
            arr[sum]++;
        }
        return ans;
    }
        '''
        if (nums == []): return 0
        count = [0] * 100001
        count[0] = 1
        prefix_sum = 0
        sol = 0
        for n in nums:
            prefix_sum += n
            if (prefix_sum - target >= 0):
                sol += count[prefix_sum - target]
            # if target is zero, adding the line below after prefix_sum+=n would interfere with the count

            count[prefix_sum] += 1
        return sol

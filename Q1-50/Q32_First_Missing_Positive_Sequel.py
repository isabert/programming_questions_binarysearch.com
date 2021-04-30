import bisect
class Solution:
    def solve(self, arr):
        #time complexity: O(logn)
        #space complexity: O(1)
        start = l = bisect.bisect(arr, 0)
        r = len(arr)-1
        if l > r:
            return 1

        while(l<=r):
            mid = (l+r)//2
            if(mid-start+1)==arr[mid]:
                l = mid+1
            else:
                # mid-start+1<arr[mid]
                if(mid==start):
                    return 1
                else:
                    #we will check the element left of mid- that element has an index of mid-1
                    if((mid-1)-start+1<arr[mid-1]):
                        r = mid-1
                    else:
                        return arr[mid-1]+1
        return len(arr)-start+1

    def solve_alt(self, arr):
        #time complexity: O(logn)
        #space complexity: O(1)
        l = 0
        r = len(arr)-1
        mid = None
        if(len(arr)==2):
            return max(arr)
        while(l<=r):
            mid = (l+r)//2
            if(r-l<=1):
                if(arr[r]>arr[l]):
                    mid = r+1
                else:
                    mid = l+1
                break
            if(arr[l]<=arr[mid] and arr[mid]<=arr[r]):
                mid = r+1
                break
            elif(arr[l]<=arr[mid]):
                l = mid
            else:
                r = mid

        return arr[mid-1]

    def solve_slowest(self, arr):
        #time complexity: O(n)
        #space complexity: O(n)
        mx = max(arr)
        flag = [False] * mx

        for i in range(len(arr)):
            flag[arr[i] - 1] = True

        res = mx + 1

        for i in range(mx):
            if (flag[i] == False):
                res = i + 1

        return res

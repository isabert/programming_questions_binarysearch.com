class Solution:
    def solve(self, arr):
        l = 0
        r = len(arr)-1
        mid = None
        if(len(arr)==2):
            return max(arr)
        while(l<=r):
            mid = (l+r)//2
            if(arr[l]<=arr[mid] and arr[mid]<=arr[r]):
                mid = r+1
                break
            elif(mid!=r and arr[mid]>arr[mid+1]):
                mid = mid+1
                break
            elif(arr[l]<=arr[mid]):
                l = mid+1
            else:
                r = mid -1

        return arr[mid-1]

    def solve_alt(self, arr):
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
class Solution:
    def solve2(self, nums):
        def sort(nums,l,r):
            if(r==l):return
            mid = (l+r)//2
            sort(nums,l,mid)
            sort(nums,mid+1,r)
            merge(nums,l,mid+1,r)

        def merge(nums,l,mid,r):
            arr = nums[:]

            nums_i =l
            i1 = l
            i2 = mid

            while(nums_i<r+1):
                if(i1==mid):
                    nums[nums_i] =arr[i2]
                    i2+=1
                elif(i2==r+1):
                    nums[nums_i]=arr[i1]
                    i1+=1
                elif(arr[i1]>arr[i2]):
                    nums[nums_i]=arr[i2]
                    i2+=1
                else:
                    nums[nums_i]=arr[i1]
                    i1+=1

                nums_i+=1

        #nums.sort()
        print(len(nums))
        sort(nums,0,len(nums)-1);
        if(len(nums)==1): return nums[0]
        dif = abs(nums[1]-nums[0])
        for i in range(1,len(nums)):
            if(abs(nums[i]-nums[i-1])>dif):
                dif = abs((nums[i]-nums[i-1]))
        return dif

    def solve(self, nums):
        nums.sort()
        if(len(nums)==1): return nums[0]
        dif = abs(nums[1]-nums[0])
        for i in range(1,len(nums)):
            if(abs(nums[i]-nums[i-1])>dif):
                dif = abs((nums[i]-nums[i-1]))
        return dif

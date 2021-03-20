class Solution:
    def solve(self, num):
        length = 0
        marker = 1

        while(num>marker):
            marker*=10
            length+=1
        print(marker)
        while(True):
            if(length==1 or length==0):return True
            lsd = num%10;
            msd = num//(marker//10);
            print(lsd)
            print(msd)
            if(lsd!=msd):return False
            num = num-msd*marker/10-lsd
            num/=10
            length-=2
            marker /= 100

s = Solution()
s.solve(43)
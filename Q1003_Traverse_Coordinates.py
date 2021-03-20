class Solution:
    def solve1(self, sx, sy, ex, ey):
        # with insights of wizwilzo:
        # for problems where we want to go from a something to a target
        # we can always look at the reverse process and see if there's greedy observations we can make
        # https://binarysearch.com/problems/Target-Number-with-Operations

        # https://binarysearch.com/problems/Target-Number-with-Operations-Sequel

        # https://binarysearch.com/problems/Make-Target-List-with-Increment-and-Double-Operations

        # https://binarysearch.com/problems/Number-of-Moves-to-Capture-the-King

        # might be overwhelming lol

        # but considering the reverse process for problems is actually a nice technique to know
        while (True):
            if (ex < sx or ey < sy): return False
            if (ex == sx):
                return (ey - sy) % ex == 0
            elif (ey == sy):
                return (ex - sx) % ey == 0

            elif (sx < ex and ex < ey):
                ey = ey % ex

            elif (sy < ey and ey < ex):
                ex = ex % ey

            else:
                return False

    def solve(self, sx, sy, ex, ey):
        while(ex>=sx and ey>=sy):
            print(ex)
            print(ey)
            if(ex>ey):
                #if the smaller one reaches boundary, return if the larger one can return to the boundary or not
                if(ey==sy):
                    return (ex-sx)%ey==0
                ex%=ey
            else:
                #ey>=ex
                if(sx==ex):
                    return (ey-sy)%sx==0
                ey%=ex
        return False
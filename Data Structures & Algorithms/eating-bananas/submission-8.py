class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        # ans lies between start and end
        ans = -1

        def check_valid(k, h):
            hrs = 0
            if(k==0):
                return False
            for p in piles:
                hrs += math.ceil(p/k)
            
            if(hrs<=h):
                return True
            else:
                return False



        while(start<=end):
            mid = (start+end)//2

            # check if eating rate is valid
            check = check_valid(mid, h)
            if check:
                ans = mid
                end = mid-1
            else:
                start = mid+1
        
        return ans

        
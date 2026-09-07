class Solution:
    
    def checkT(self, arr, k, h):
        time = 0
        for n in arr:
            time += math.ceil(n/k)
        
        return True if time<=h else False

    def giveK(self, arr, start, end, h):
        if (start>=end):
            return -1
        mid = (start + end)//2
        k_mid = arr[mid]
        out_mid = self.checkT(arr, k_mid, h)
        if not out_mid:
            return self.giveK(arr, mid+1, end, h)
        else:
            ans = k_mid
            left = self.giveK(arr, start, mid-1, h)
            if left>0:
                checkleft = self.checkT(arr, left, h)
                return min(k_mid, left) if checkleft else k_mid
            else:
                return k_mid

    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        K_min = min(piles)
        K_max = max(piles)
        # new_K = [x for x in range(1, K_max+1)]
        start = 1
        end = K_max
        ans = K_max
        while(start<=end):
            mid = (start+end)//2
            k_mid = mid
            time = sum(math.ceil(x/k_mid) for x in piles)
            if time<=h:
                ans = k_mid
                end = mid-1
            else:
                start = mid+1
        return ans



        # find num such that, k is min
        # each entry eating time = math.ceil(num/k)
        # total time = sum(t)
        # total time<= h
        # smallest k for 



        
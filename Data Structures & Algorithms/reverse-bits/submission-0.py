class Solution:
    def setBitAt(self, n, i):
        mask = 1<<i
        n = n | mask
        return n
    
    def reverseBits(self, n: int) -> int:
        # lets find all indixes from right to left
        # of set bits, and in the last and then 32-ith bit should be set
        ans = 0
        i = 0
        while(n>0):
            last_bit = n & 1
            if last_bit:
                ans = self.setBitAt(ans, 31-i)
            n = n>>1
            i += 1
        return ans
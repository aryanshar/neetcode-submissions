class Solution:
    def count_setBits(self, n:int):
        count = 0
        while(n>0):
            # flips the bits till last set bit
            n = n & (n-1)
            count += 1
        return count
    
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(0, n+1):
            output.append(self.count_setBits(i))
        return output
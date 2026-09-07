class Solution:
    
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        def climb(dp, n):
            if n<0:
                return 0
            if n==0 or n==1:
                return 1
            
            if(dp[n]!=0):
                return dp[n]
            
            dp[n] = climb(dp, n-1) + climb(dp, n-2)
            return dp[n]

        return climb(dp, n)
        
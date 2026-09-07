class Solution:
    
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        def climb(dp, i, n):
            dp[0] = dp[1] = 1
            for i in range(2, n+1):
                dp[i] = dp[i-1]+dp[i-2]

            return dp[n]
        return climb(dp, 0, n)
            # if n<0:
            #     return 0
            # if n==0 or n==1:
            #     return 1
            
            # if(dp[n]!=0):
            #     return dp[n]
            
            # dp[n] = climb(dp, n-1) + climb(dp, n-2)
            # return dp[n]

        return climb(dp, n)
        
class Solution:
    def checkdp(self, n, dp):
        if (n==1 or n==2):
            return n
        if n in dp:
            return dp[n]
        dp[n] = self.checkdp(n-1,dp) + self.checkdp(n-2,dp)
        return dp[n]
    
    def climbStairs(self, n: int) -> int:
        dp = {}
        return self.checkdp(n, dp)


        
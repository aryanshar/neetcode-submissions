class Solution:
    def costPath(self, cost, i, n, dp):
        if (n==1 or n==0):
            return 0
        x = 0
        y = 0
        if dp[n-i-1]!=0:
            x = dp[n-i-1]
        else: x = self.costPath(cost, i, n-i-1, dp)
        if dp[n-i-2]!=0:
            y = dp[n-i-2]
        else: y = self.costPath(cost, i, n-i-2, dp)
        dp[n] =  min(cost[n-i-1]+x, cost[n-i-2]+y)
        return dp[n]
        
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*(n+1)
        return self.costPath(cost, 0, n, dp)
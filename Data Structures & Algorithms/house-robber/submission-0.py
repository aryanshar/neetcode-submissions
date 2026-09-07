class Solution:
    def money(self, nums, i, n, dp):
        if(i>=n):
            return 0
        if(dp[i]!=0):
            return dp[i]
        # recursive case
        dp[i] = max(nums[i]+self.money(nums, i+2, n, dp), self.money(nums, i+1, n, dp))
        return dp[i]
    
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums))
        return self.money(nums, 0, len(nums), dp)
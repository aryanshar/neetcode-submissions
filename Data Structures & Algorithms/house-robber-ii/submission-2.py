class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+1)
        def search(nums, i, n, dp):
            if len(nums) == 1:
                return nums[0]
            if(n<i):
                return 0
            if(n==i):
                return nums[n]
            
            if(dp[n]):
                return dp[n]
            
            dp[n] = max(search(nums, i, n-1, dp), search(nums, i,n-2, dp)+nums[n])

            return dp[n]
        dp1 = [0]*(len(nums)+1)
        dp2 = [0]*(len(nums)+1)
        return max(search(nums, 0, len(nums)-2, dp1), search(nums, 1, len(nums)-1, dp2))
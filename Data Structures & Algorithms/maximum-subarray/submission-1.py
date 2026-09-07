class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = j = 0
        n = len(nums)
        curr_sum = 0
        max_sum = -9999999

        while(j<n):
            curr_sum = curr_sum + nums[j]
            if(curr_sum<nums[j]):
                i=j
                curr_sum = nums[i]
            max_sum = max(max_sum, curr_sum)
            j += 1
        
        return max_sum
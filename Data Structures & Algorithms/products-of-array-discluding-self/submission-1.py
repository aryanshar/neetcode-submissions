class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_left, prefix_right = [1]*len(nums), [1]*len(nums)

        for i in range(1, len(nums)):
            prefix_left[i] = prefix_left[i-1]*nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            prefix_right[i] = prefix_right[i+1]*nums[i+1]
        
        for i, n in enumerate(nums):
            prefix_right[i] = prefix_right[i]*prefix_left[i]

        return prefix_right
        
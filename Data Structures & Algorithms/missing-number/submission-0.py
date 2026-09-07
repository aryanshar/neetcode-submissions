class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # range: 0 -> n

        all_xor  = 0
        missing_xor = 0
        for num in range(n+1):
            all_xor = all_xor ^ num
        
        for num in nums:
            missing_xor = missing_xor^num

        missing_num = all_xor^missing_xor
        return missing_num
        
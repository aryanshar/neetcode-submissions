class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_freq = {}
        for num in nums:
            if num in nums_freq.keys():
                return True
            else:
                nums_freq[num] = 1
        return False
        
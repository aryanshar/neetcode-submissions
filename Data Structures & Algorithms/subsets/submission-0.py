class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if(len(nums) == 0):
            return []

        def genall(nums, i, n):
            if(i==n):
                return [[]]
            without = genall(nums, i+1, n)
            with_ = [[nums[i]] + list(ele) for ele in without]
            return with_ + without

        
        return genall(nums, 0, len(nums))

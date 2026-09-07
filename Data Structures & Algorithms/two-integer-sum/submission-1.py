class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx = {}
        ans = [-1, -1]            
        
        for i, num in enumerate(nums):
            secNum = target - num
            if secNum in nums_idx.keys():
                ans =  [nums_idx[secNum][0],i]
            elif num in nums_idx.keys():
                nums_idx[num].append(i)
            else:
                nums_idx[num] = [i]
        return ans    
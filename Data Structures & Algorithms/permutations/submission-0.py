class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def perm(nums, i, n):

            # base case
            if(i==n):
                # store output and return
                # swap back the change and return
                res.append(nums.copy())
                return
            
            for j in range(i,n):
                nums[i], nums[j] = nums[j], nums[i]
                perm(nums, i+1, n)
                nums[i], nums[j] = nums[j], nums[i]
        perm(nums, 0, len(nums))
        return res
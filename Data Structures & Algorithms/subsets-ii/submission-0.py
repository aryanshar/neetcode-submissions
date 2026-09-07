class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def subs(nums, i, n):
            # base case
            if(i==n):
                return [[]]
            
            pick_i = [[nums[i]] + x for x in subs(nums, i+1, n)]
            # not pick i when? dedup
            new_i = i+1
            while(new_i!=n and nums[new_i]==nums[i]):
                new_i += 1
            not_i = subs(nums, new_i, n)
            return pick_i + not_i
        return subs(nums, 0, len(nums))
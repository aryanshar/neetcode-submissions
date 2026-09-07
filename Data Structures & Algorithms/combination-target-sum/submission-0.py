class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def find_comb(nums, i, n, target, output):

            if(i==n or target<0):
                # finished the array
                return []
            if(target==0):
                return [output]
            
            pick_i = find_comb(nums, i, n, target-nums[i], output+[nums[i]])
            not_pick_i = find_comb(nums, i+1, n, target, output)

            return pick_i + not_pick_i
                
        return find_comb(nums, 0, len(nums), target, [])            
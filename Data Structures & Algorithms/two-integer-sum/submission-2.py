class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        output = []
        for i,n in enumerate(nums):
            if(target-n in store):
                first = store[target-n]
                second = i
                output.append(first)
                output.append(second)
            store[n] = i
        
        return output
        
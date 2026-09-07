class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_store = {}
        if not nums:
            return 0
        for num in nums:
            if num in nums_store:
                nums_store[num] += 1
            else:
                nums_store[num] = 1
        count_max = 1
        for num in nums:
            count = 1
            next_num = num+1
            while(next_num in nums_store):
                next_num += 1
                count += 1
                count_max = max(count_max, count)


        return count_max
        
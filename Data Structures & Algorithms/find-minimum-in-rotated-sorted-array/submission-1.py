class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        mini = 999999999999
        def check(nums, start, end, mini):
            if (start>end):
                return mini
            print(f"mini is {mini}, start is {start}, end is {end}\n")
            mid = (start+end)//2
            x = nums[mid]
            if x<mini:
                mini = x
            if (mid>start and nums[mid-1] > x) and (mid<end and nums[mid+1] > x):
                return mini
            mini=min(check(nums, start, mid-1, mini), check(nums, mid+1, end, mini))
            return mini
        return check(nums, start, end, mini)
        
class Solution:
    def find_num(self, nums, start, end, target):
        mid = (start+end)//2
        if(start>end):
            return -1
        elif(nums[mid]==target):
            return mid
        
        elif(nums[mid]>target):
            return self.find_num(nums, start, mid-1, target)
        else:
            return self.find_num(nums, mid+1, end, target)
    
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums)-1
        return self.find_num(nums, s, e, target)
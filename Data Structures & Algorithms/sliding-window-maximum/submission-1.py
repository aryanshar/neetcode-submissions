class Solution:
    def maxWindow(self, arr: List[int]) -> int:
        maxi = -1
        for num in arr:
            maxi = max(maxi, num)
        return maxi
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        maxi_len = n - k + 1

        maxi = [-1]*maxi_len if maxi_len>0 else None

        i = 0
        while(i<maxi_len):
            sub_max = self.maxWindow(nums[i:i+k])
            maxi[i] = sub_max
            i +=1

        return maxi

        
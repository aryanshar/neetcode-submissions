class Solution:
    def binsearch(self, nums, k, start, end):
        if(start>end):
            return -1
        mid = (start+end)//2
        if nums[mid]==k:
            return mid
        if k>nums[mid]:
            return self.binsearch(nums,k,mid+1, end)
        else:
            return self.binsearch(nums,k,start, mid-1)
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1
        k = target
        ans = -1
        while(l<=r):
            mid = l + (r-l)//2
            if (nums[mid]==k):
                ans = mid
                return ans
            x = nums[mid]
            if x < nums[r]:
                # right half is sorted
                chk = self.binsearch(nums,k,mid+1, r)
                if chk ==-1:
                    r = mid-1
                else:
                    return chk

            else:
                # left half is sorted
                chk = self.binsearch(nums,k,l, mid-1)
                if chk==-1:
                    l = mid+1
                else:
                    return chk
            # if x < k:
            #     # go in increasing order
            #     if x > nums[r]:
            #         # go left
            #         r = mid - 1
            #     else:
            #         l = mid + 1
            # else:
            #     if x > nums[r]:
            #         l = mid + 1
            #     else:
            #         r = mid - 1
        return ans
        
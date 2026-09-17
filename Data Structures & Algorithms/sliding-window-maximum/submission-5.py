class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        window = {}
        max_ele = float('-inf')
        for i in range(k):
            if nums[i] in window:
                window[nums[i]] += 1
            else:
                window[nums[i]] = 1
            max_ele = max(max_ele, nums[i])
        res.append(max_ele)

        for i in range(k, len(nums)):
            new = nums[i]
            old = nums[i-k]

            # if old==max_ele and new<max_ele:
            #     max_ele = 0
            #     for j in range(i-k+1, i):
            #         max_ele = max(nums[j], max_ele)
            # else:
            #     max_ele = new
            
            if new not in window:
                window[new] = 1
            else:
                window[new] += 1
            
            window[old] -= 1

            if window[old] == 0:
                del window[old]
            
            max_ele = max(window)
            # if new>max_ele:
            #     max_ele = new
            #     res.append(new)
            #     window[old] -= 1
            # else:
            #     if old==max_ele:
            #         # O(k)
            res.append(max_ele)

        return res 



        
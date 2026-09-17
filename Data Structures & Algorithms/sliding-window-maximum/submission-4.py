import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        window = []
        for i in range(k):
            heapq.heappush(window, (-nums[i], i))
        
        res.append(-window[0][0])
        for j in range(k, len(nums)):
            # heapq.heappop(window)
            heapq.heappush(window, (-nums[j], j))
            while(window[0][1] <= j-k):
                heapq.heappop(window)
            res.append(-window[0][0])
        
        return res
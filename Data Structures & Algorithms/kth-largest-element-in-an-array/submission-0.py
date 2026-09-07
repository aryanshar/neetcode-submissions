import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k] if k<len(nums) else nums
        heapq.heapify(heap)

        for i in range(k, len(nums)):
            top = heap[0]
            if(nums[i]>top):
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
        
        return heap[0]
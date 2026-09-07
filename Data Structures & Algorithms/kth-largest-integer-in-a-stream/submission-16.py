import heapq
class KthLargest:

    # def __init__(self, k: int, nums: List[int]):
    #     self.k = k
    #     self.nums = [-1*x for x in nums]
    #     self.heap = self.nums
    #     heapq.heapify(self.heap)

    # def add(self, val: int) -> int:
    #     heapq.heappush(self.heap, -val)
    #     return -1*heapq.nsmallest(self.k, self.heap)[-1]

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums if k>len(nums) else nums[:k]
        heapq.heapify(self.heap)
        for i in range(k, len(nums)):
            if nums[i]>self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, nums[i])
        

    def add(self, val: int) -> int:
        if len(self.heap)==self.k and val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
            return self.heap[0]
        elif len(self.heap)<self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        else:
            return self.heap[0]

        
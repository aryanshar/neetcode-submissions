import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-1*x for x in nums]
        self.heap = self.nums
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        return -1*heapq.nsmallest(self.k, self.heap)[-1]

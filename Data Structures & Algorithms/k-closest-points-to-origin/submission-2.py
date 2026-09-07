import numpy as np
import heapq as heap
class Solution:
    def dist(self, pointA):
        return math.sqrt(pointA[0]**2 + pointA[1]**2)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # make a min heap of first k points, and iterate through rest of points
        # remove min element from heap, where element is heap is euc_dist from origin
        h = points[:k] if k < len(points) else points
        h = [(-self.dist(p), p) for p in h]
        heap.heapify(h)
        for i in range(k, len(points)):
            top = h[0]

            if(abs(self.dist(points[i]))<abs(top[0])):
                heap.heappop(h)
                heap.heappush(h, (-self.dist(points[i]),points[i]))
        
        # in the end this will always have the maximum k elements in sorted order

        out = [x[1] for x in h]
        return out
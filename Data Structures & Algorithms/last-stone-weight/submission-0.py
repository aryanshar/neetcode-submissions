import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-x for x in stones]
        heapq.heapify(q)
        while(len(q)>1):
            top1 = heapq.heappop(q)
            top2 = heapq.heappop(q)
            new_sum = abs(top1-top2)
            heapq.heappush(q, -new_sum)
        
        if(len(q)):
            return -q[-1]
        return 0
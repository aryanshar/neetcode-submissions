class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        visited = []
        for start, end in intervals:
            if not visited:
                visited.append([start,end])
            if(start<=visited[-1][1] or start==visited[-1][0]):
                visited[-1][1] = max(end, visited[-1][1]) 
            else:
                visited.append([start, end])
        return visited
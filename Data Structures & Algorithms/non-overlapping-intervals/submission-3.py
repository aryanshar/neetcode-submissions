class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        visited = []
        intervals.sort(key=lambda x:x[1])
        for interval in intervals:
            start, end = interval[0], interval[1]
            if not visited:
                visited.append([start,end])
                continue
            old_start = visited[-1][0]
            old_end = visited[-1][1]
            if start < old_end:
                # visited[-1][1] = end
                count += 1
            else:
                visited.append([start, end])
        return count
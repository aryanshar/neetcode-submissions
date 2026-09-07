class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxi = 0
        while(i<j):
            water = min(heights[i], heights[j])*(j - i)
            maxi = max(maxi, water)
            if heights[i] <= heights[j]:
                i +=1
            else:
                j -=1

        return maxi
            
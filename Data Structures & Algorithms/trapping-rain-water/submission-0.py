class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        leftH, rightH = [height[0]]*n, [height[n-1]]*n
        for i in range(1,n):
            leftH[i] = max(leftH[i-1], height[i])
        for j in range(n-2, 0, -1):
            rightH[j] = max(rightH[j+1], height[j])
        
        water = 0
        for i in range(1, n-1):
            water += min(leftH[i], rightH[i]) - height[i]
        

        return water
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_h = [0]*n
        right_h = [0]*n

        i = 0
        j = len(height)-1
        max_left_h = 0
        max_right_h = 0
        while(i<len(height)):
            max_left_h = max(max_left_h, height[i])
            left_h[i] = max_left_h
            max_right_h = max(max_right_h, height[j])
            right_h[j] = max_right_h
            i += 1
            j -= 1
        
        total_water = 0
        
        for i,h in enumerate(height):
            w_h = max(min(left_h[i], right_h[i]) - h, 0)
            total_water += w_h

        return total_water
        
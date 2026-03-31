class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        for i in range(1, len(height)):
            left_max = (max(height[:i+1]))
            right_max = (max(height[i:]))
            result = result + (min(left_max, right_max) - height[i])
        return result
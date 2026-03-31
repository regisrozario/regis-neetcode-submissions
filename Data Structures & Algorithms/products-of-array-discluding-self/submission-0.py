class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        index = 0
        result = []
        while index < len(nums):
            left_temp = nums[:index]
            left_prod = math.prod(left_temp)
            right_temp = nums[index + 1 :]
            right_prod = math.prod(right_temp)
            result.append(left_prod * right_prod)
            index += 1
        return result
        
        
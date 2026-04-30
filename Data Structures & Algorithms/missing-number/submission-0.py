class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i, val in enumerate(nums):
            temp = i ^ val
            res = res ^ temp
        
        return res
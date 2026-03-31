class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*(2*len(nums))
        for i in range(len(nums)):
            result[i] = result[i+n] = nums[i]
        
        return result

        
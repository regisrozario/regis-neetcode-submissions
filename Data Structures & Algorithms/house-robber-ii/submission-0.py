class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        rob1,rob2 = 0,0
        for i in range(len(nums)-1):
            curr = max(rob2 + nums[i], rob1)
            rob2 = rob1
            rob1 = curr
        max1 = rob1
        rob1,rob2 = 0,0
        for i in range(1, len(nums)):
            curr = max(rob2 + nums[i], rob1)
            rob2 = rob1
            rob1 = curr
        max2 = rob1

        return max(max1,max2)
        
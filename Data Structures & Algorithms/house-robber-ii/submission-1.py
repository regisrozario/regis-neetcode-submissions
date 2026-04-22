class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(nums, start, end):
            rob1,rob2 = 0,0
            for i in range(start,end):
                curr = max(rob2 + nums[i], rob1)
                rob2 = rob1
                rob1 = curr
            return rob1

        return max(helper(nums, 0, len(nums)-1),helper(nums, 1, len(nums)))
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2 = 0,0
        for i in range(len(nums)):
            curr = max(rob2+nums[i], rob1)
            rob2 = rob1
            rob1 = curr
        return rob1

        
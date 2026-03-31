class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i in range(len(nums)):
            val = target - nums[i]
            if val in seen:
                index = nums.index(val)
                return [index, i]
            else:
                seen.add(nums[i])
        

        
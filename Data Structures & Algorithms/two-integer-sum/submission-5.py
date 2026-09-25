class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            temp = target - n
            if temp in seen:
                return [seen[temp], i]
            seen[n] = i
        return []
        
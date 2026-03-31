class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}
        for i, n in enumerate(nums):
            val = target - n
            if val in seenMap:
                return [seenMap[val], i]
            seenMap[n] = i
        return[]
        

        
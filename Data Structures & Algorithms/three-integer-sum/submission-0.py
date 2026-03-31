class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = defaultdict(list)
        for i, n in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = n + nums[left] + nums[right]
                if s == 0:
                    if (n, nums[left], nums[right]) not in res:
                        res[(n, nums[left], nums[right])] = [n, nums[left], nums[right]]
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return [x for x in res.values()]
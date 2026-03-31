class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in nums:
                count = 0
                m = n
                while m in nums:
                    count +=1
                    m +=1
                longest = max(longest, count)
        
        return longest



        
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i, curr):
            if i >= len(nums):
                res.append(curr[:])
                return
            dfs(i+1, curr)
            curr.append(nums[i])
            dfs(i+1,curr)
            curr.pop()
        dfs(0, curr)
        return list(set([tuple(sorted(x)) for x in res]))
        

        
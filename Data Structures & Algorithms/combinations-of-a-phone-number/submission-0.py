class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(index, temp):
            if index == len(digits):
                res.append("".join(temp))
                return
            letters = mapping[digits[index]]
            for c in letters:
                temp.append(c)
                dfs(index+1, temp)
                temp.pop()
        
        dfs(0, [])
        return res
            

            

        
        
class Solution:
    def isValid(self, s: str) -> bool:
        val = {"]": "[", ")": "(", "}": "{"}
        stack = []
        for ch in s:
            if ch in val.values():
                stack.append(ch)
            else:
                if len(stack) == 0 or val[ch]!=stack.pop():
                    return False

        return len(stack) == 0
class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(word)}#{word}" for word in strs])

    def decode(self, s: str) -> List[str]:
        right = 0
        result = []
        while right < len(s):
            pointer = right
            curr_limit_val = s.index('#',right)
            count = int(s[pointer:curr_limit_val])
            word = s[curr_limit_val+1: curr_limit_val+1+count]
            right = curr_limit_val+1+count
            result.append(word)
        return result

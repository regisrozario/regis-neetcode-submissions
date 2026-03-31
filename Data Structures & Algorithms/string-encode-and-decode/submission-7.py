class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(word)}#{word}" for word in strs])

    def decode(self, s: str) -> List[str]:
        right = 0
        result = []
        while right < len(s):
            digit,right = self.get_digits(s, right)
            curr = right+1
            result.append(s[curr: curr+digit])
            right = curr+digit
        return result



    def get_digits(self, s:str, right: int):
        curr = right
        while s[right] != "#":
            right +=1
        return (int(s[curr:right]), right)

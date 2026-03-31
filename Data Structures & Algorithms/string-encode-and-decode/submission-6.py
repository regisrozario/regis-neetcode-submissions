class Solution:

    def encode(self, strs: list[str]) -> str:
        final = ""
        for s in strs:
            temp = len(s)
            final += str(temp) + "#" + s
        return final

    # 4#neet4#code
    def decode(self, s: str) -> list[str]:
        l = 0
        result = []
        while l < len(s):
            d = l
            while s[d] != "#":
                d += 1
            count = int(s[l:d])
            l = d + 1
            word = s[l : l + count]
            result.append(word)
            l = l + count
        return result
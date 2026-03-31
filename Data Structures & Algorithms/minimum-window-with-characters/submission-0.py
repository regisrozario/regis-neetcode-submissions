class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq,count = {},{}
        for c in t:
            count[c] = count.get(c,0)+1
        have,need = 0,len(count)
        left = 0
        res, length = [-1,-1],len(s) + 1

        for right in range(len(s)):
            c = s[right]
            freq[c] = freq.get(c,0) + 1
            if c in count and freq[c] == count[c]:
                have +=1
            
            while have == need:
                if (right - left +1) < length:
                    length = (right - left +1)
                    res = [left, right +1]
                freq[s[left]] -= 1
                if s[left] in count and freq[s[left]] < count[s[left]]:
                    have -=1
                left +=1
        return s[res[0]:res[1]]



        
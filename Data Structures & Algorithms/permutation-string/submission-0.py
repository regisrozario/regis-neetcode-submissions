class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        c1, c2 = {},{}
        for i in range(len(s1)):
            c1[s1[i]] = 1 + c1.get(s1[i],0)
            c2[s2[i]] = 1 + c2.get(s2[i],0)
        
        left,right = 0,len(s1)-1

        while right < len(s2):
            if c1 == c2:
                return True
            left_char = s2[left]
            c2[left_char] -=1
            if c2[left_char] == 0:
                c2.pop(left_char)
            right +=1
            left +=1
            
            if right < len(s2):
                c2[s2[right]] = 1+ c2.get(s2[right],0)
        
        return False
        
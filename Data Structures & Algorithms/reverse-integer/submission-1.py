class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31
        MAX = 2**31 - 1
        rev = 0
        initial_val = x
        x = abs(x)

        while x:
            d, m = divmod(x, 10)
            if rev > MAX // 10 or (rev == MAX //10 and m > 7):
                return 0
            if rev < MIN // 10 or (rev == MIN // 10 and m > 8):
                return 0
            rev = rev * 10 + m
            x = d
            
        
        return -1*rev if initial_val < 0 else rev
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        initial_val = x
        x = abs(x)

        while x:
            d, m = divmod(x, 10)
            rev = rev * 10 + m
            x = d
        
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        
        return -1*rev if initial_val < 0 else rev
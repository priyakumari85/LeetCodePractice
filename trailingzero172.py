class Solution:
    def trailingZeroes(self, n: int) -> int:
        #counter = 0
        #out = 0
        #if 5**counter<=n:
        #    out = out + (n/5**counter)
        #    counter+=1
        #return int(out)
        res = 0
        while n > 0:
            n = n // 5
            res += n
        return res

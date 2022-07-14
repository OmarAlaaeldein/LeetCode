class Solution:
    def reverse(self, x: int) -> int:
        x=list(str(x))[::-1]
        if x[-1]=='-':
            x.pop()
            s=-1*int(''.join(x))
        else:
            s=int(''.join(x))
        if (s<-2**31) or (s>(2**31)-1):
            return 0
        else:
            return s
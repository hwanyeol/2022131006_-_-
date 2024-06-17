class Solution:
    def balancedStringSplit(self, s: str) -> int:
        a=0
        b=0
        c=0
        for i in s:
            if i=='L':
                a=a+1
            else:
                b=b+1
            if a==b:
                c=c+1
        return c
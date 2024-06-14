class Solution:
    def setdata(self,first,second):
        n=len(first)
        for i in range(n):
            for j in range(i+1,n+1):
                if first[i]+first[j]==second:
                    return print([i,j])
        
a=Solution()
a.setdata([2,7,11,15],9)

class Solution:
    def addTwoNumbers(self, l1, l2):
        self.l1=l1
        self.l2=l2
        a=0
        b=[]
        for i in range(len(l1)):
            a=l1[i]*10^i+a
        for i in range(len(l2)):
            a=a+l2[i]*10^i
        for i in range(len(str(a))):
            b.append(a%10)
            a=a//10
        return b
c=Solution()
print(c.addTwoNumbers([2,4,3],[5,6,4]))
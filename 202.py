class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  
        while n != 1:
            if n in seen:  # 이미 본 숫자를 만나면, 순환에 빠진 것
                return False
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))  
        return True 

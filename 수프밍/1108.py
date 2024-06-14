class Solution:
    def defangIPaddr(self, address: str) -> str:
        self.address=address
        b=address.replace('.','[.]')
        return b
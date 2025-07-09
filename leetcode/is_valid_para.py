class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            l = len(s)
            s = s.replace('()','')
            s=s.replace('{}','')
            s=s.replace('[]','')
            if l==len(s): 
                return False
            print(s)
        return True
        
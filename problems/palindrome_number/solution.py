class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        
        multiple=1
        while x>=multiple*10:
            multiple*=10
        while x>9 and multiple>1:
            right=x%10
            left=(x//multiple)%10
            if left!=right: return False
            multiple//=100
            x//=10
        return True
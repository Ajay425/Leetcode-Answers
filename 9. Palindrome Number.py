class Solution:
    def isPalindrome(self, x: int) -> bool:
        res=str(x)
        if res[::-1] == str(x):
            return True
        else:
            return False

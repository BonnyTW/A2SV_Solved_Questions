class Solution:
    def isPalindrome(self, x: int) -> bool:

        temp=x
        reversednum=0
        while temp>0:
            lastd=temp%10
            reversednum=reversednum*10+lastd
            temp//=10
        return x==reversednum

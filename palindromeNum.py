# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0 or x%10 ==0 and x!=0:
            return False
        
        reversed_half = 0
        
        while(reversed_half<x):
            reversed_half = reversed_half*10
            last_digit = x%10
            reversed_half+=last_digit
            x = x//10
 
        if reversed_half==x or reversed_half//10==x:
            return True
        else:
            return False
            
        

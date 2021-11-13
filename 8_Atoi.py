# 8. String to Integer (atoi)

# Refer to https://www.youtube.com/watch?v=zwZXiutgrUE

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        '''        
        Time O(n)
        Space O(1)
        
        n is the number of characters in your input string
        '''
        
        MAX_INT = 2 ** 31 - 1 # 2147483647
        MIN_INT = -2 ** 31    #-2147483648
 
        i = 0
        res = 0
        negative = 1
        
        #whitespace
        while i < len(str) and str[i] == ' ':
            i += 1
        
        #+/- symbol
        if i < len(str) and str[i] == '-':
            i += 1
            negative = -1
        elif i < len(str) and str[i] == '+':
            i += 1
     
        #check number 0-9
        checker = set('0123456789')
        while i < len(str) and str[i] in checker:
            if (res > MAX_INT // 10) or (res == MAX_INT // 10 and int(str[i]) > 7):
                return MAX_INT if negative == 1 else MIN_INT
            res = res * 10  + int(str[i])
            i += 1
        
        #check the MAX / MIN int
        return res * negative
    
    
    
    
    

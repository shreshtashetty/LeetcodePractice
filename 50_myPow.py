# 50. Pow(x, n)

#--------------MY JUNK---------------------------------

import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(4)

def Pow(x, n, num):
    
    if n==0 or num==0.0:
        return num

    num = num*x
    n-=1

    return Pow(x, n, num)

# -------------------------------------------------------

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # In order to avoid time limit error with iterations and 
        # Recursion depth error with recursion
        
        log_y = n * math.log10(abs(x)) # Take abs(x) because log(-x) is invalid
        ans = 10 ** log_y
		
        if x < 0:
		    # Choose the right sign for the ans
			# If you multiply -ve number even number of times, sign will be +ve; otherwise -ve
            if n%2==1:
                ans*=-1
			
        return ans
    
#   ---------------------------------------
#         # Iterative
#         num = 1
#         if n<0:
#             x = 1/x
#             n*=-1
#         for i in range(n):
#             num = num*x
            
#         return num
#   ---------------------------------------            
#         # Recursive 

#         if n>=0:
#             return Pow(x, n, 1)
        
#         else:
#             return Pow(1/x, n*-1, 1)
#   ---------------------------------------
        

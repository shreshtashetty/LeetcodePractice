# 22. Generate Parentheses

# Refer to Nick White's video.
# Solution with Backtracking.

def backtrack(res, curr, open_, close_, n):
    if len(curr)==n*2:
        res.append(curr)
        return
    
    if open_<n:
        backtrack(res, curr+"(", open_+1, close_, n)
    if close_<open_:
        backtrack(res, curr+")", open_, close_+1, n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        backtrack(res, "", 0, 0, n)
        return res
        


# # Solution without backtracking
# class Solution:
#     def generateParenthesis(self, n):
#         def generate(A = []):
#             if len(A) == 2*n:
#                 if valid(A):
#                     ans.append("".join(A))
#             else:
#                 A.append('(')
#                 generate(A)
#                 A.pop()
#                 A.append(')')
#                 generate(A)
#                 A.pop()

#         def valid(A):
#             bal = 0
#             for c in A:
#                 if c == '(': bal += 1
#                 else: bal -= 1
#                 if bal < 0: return False
#             return bal == 0

#         ans = []
#         generate()
#         return ans

# LAME ATTEMPT(WRONG SOLUTION)    
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         if n == 1:
#             return ['()']
        
#         l = self.generateParenthesis(n-1)
#         l_ = []
#         for i in range(len(l)):
#             if l[i]+'()' not in l_:
#                 l_.append(l[i]+'()')
               
#             if '()'+l[i] not in l_:
#                 l_.append('()'+l[i])
            
#             if '('+l[i]+')' not in l_:
#                 l_.append('('+l[i]+')')
#         print(len(l_), len(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]))       
#         return l_

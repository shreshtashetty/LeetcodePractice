# 17. Letter Combinations of a Phone Number

def letterCombinationsRecursive(result, digits, current, index, mapping):
    if index == len(digits):
        result.append(current)
        return 

    letters = mapping[int(digits[index])]
    for i in range(len(letters)):
        letterCombinationsRecursive(result, digits, current + letters[i], index+1, mapping)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if digits is None or len(digits)==0:
            return result
        mapping = {0:"0", 1:"1", 2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        
        letterCombinationsRecursive(result, digits, "", 0, mapping)
        return result
    
    
            

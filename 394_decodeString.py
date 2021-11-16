# 394. Decode String

# Nick White's Solution: https://www.youtube.com/watch?v=0iQqj5egK9k

class Solution:
    def decodeString(self, s: str) -> str:
        
        counts = []
        results = []
        res = ""
        index = 0
        
        while(index<len(s)):
            
            if s[index].isdigit():
                count = 0
                while(s[index].isdigit()):
                    count = count*10 + int(s[index])
                    index+=1
                counts.append(count)
                
            elif s[index] == '[':
                results.append(res)
                res = ''
                index+=1
                
            elif s[index] == ']':
                temp = results.pop()
                count = counts.pop()
                for i in range(count):
                    temp+=res
                res = temp
                index+=1
                
            else:
                res+=s[index]
                index+=1
                
        return res

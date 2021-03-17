# 443. String Compression

class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        i = 0
        j = 0

        while(i<len(chars)):
            
            while(j<len(chars) and chars[i]==chars[j]):
                j+=1
            
            count = j-i
            s+=chars[i]
            if count>1:
                s+=str(count)

            i = j
            j +=1  

        for i in range(len(s)):
            chars[i] = s[i]
            
        return len(s)
            

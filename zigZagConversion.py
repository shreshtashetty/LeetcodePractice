#6. ZigZag Conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = []
        for i in range(numRows):
            l.append([])
        row=0
        direc = 1

        for i in range(len(s)):
            if(direc == -1):
                l[row]+=s[i]
                row-=1
                if(row<0):
                    row = row+2
                    direc = 1
                    continue
            
            if(direc == 1):
                l[row]+=s[i]
                row+=1
                if(row==len(l)):
                    row = row-2
                    direc = -1
            
        str2=''
        for i in range(len(l)):
            str1 = ''.join(l[i])
            print(str1)
            str2+=str1
            
        return str2
        

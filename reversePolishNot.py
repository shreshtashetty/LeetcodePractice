# 150. Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        
        while(len(tokens)>1):
            for i in range(len(tokens)):
                if tokens[i]=="+" or tokens[i]=="-" or tokens[i]=="*" or tokens[i]=="/":
                    if tokens[i]=="+":
                        val = int(tokens[i-2]) + int(tokens[i-1])
                    if tokens[i]=="-":
                        val = int(tokens[i-2]) - int(tokens[i-1])
                    if tokens[i]=="*":
                        val = int(tokens[i-2]) * int(tokens[i-1])
                    if tokens[i]=="/":
                        val = int(int(tokens[i-2]) / int(tokens[i-1]))
                    tokens[i-2:i+1] = [val]
                    break
        return tokens[0]
        

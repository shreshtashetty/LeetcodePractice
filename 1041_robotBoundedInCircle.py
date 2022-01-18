# 1041. Robot Bounded In Circle

# Neetcode: https://www.youtube.com/watch?v=nKv2LnC_g6E

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        '''
        # Cases
        "GLGLGGLGL"
        "GGLLGG"
        "GL"
        '''
        L,R = {},{}
        # north, west, south, east: 0, 1, 2, 3
        L = {0:1, 1:2, 2:3, 3:0} # given original dir and L instr, resulting dir
        R = {0:3, 1:0, 2:1, 3:2} # given original dir and R instr, resulting dir
        
        pos = [0,0]
        direc = 0

        for i in instructions:
            
            if i=='G':
                if direc==0:
                    pos[1]+=1
                elif direc==1:
                    pos[0]-=1
                elif direc==2:
                    pos[1]-=1
                elif direc==3:
                    pos[0]+=1
            elif i=='L':
                direc = L[direc]
            elif i=='R':
                direc = R[direc] 

        return pos==[0,0] or direc!=0

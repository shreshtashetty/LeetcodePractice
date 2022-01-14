# 3. Longest Substring Without Repeating Characters

'''
"aabaab!bb"
"tmmzuxt"
"suqqjkuuxfeinpgjucmoc"
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)==0:
            return 0
        
        if len(s)==1:
            return 1
        
        p1 = 0
        l = 0
        hashmap = {}
        
        for i in range(1, len(s)+1):

            sub = s[p1:i]
            
            if len(sub)!=len(set(sub)):
                p1 = hashmap[s[i-1]]+1
                sub = s[p1:i]
     
            hashmap[s[i-1]] = i-1
            
            if len(sub)==len(set(sub)):
                l = max(l, len(sub))
                    
        return l
    
#         # ANOTHER SOLUTION (MY OLD ONE)                    
#         seq=''
#         # seqs=[]
#         max_len = 0
#         for i in range(len(s)):
#             if(s[i] not in seq):
#                 seq+=s[i]
#             else:
#                 # print("in s[i]")
#                 ind = max([key for key, value in enumerate(seq) if value == s[i]])
#                 seq = seq[ind+1:]+s[i]

#             # seqs.append(seq)
#             if(len(seq)>max_len):
#                     max_len = len(seq)
            
#         # print(seqs)
#         return max_len

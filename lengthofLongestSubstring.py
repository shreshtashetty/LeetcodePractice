class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seq=''
        # seqs=[]
        max_len = 0
        for i in range(len(s)):
            if(s[i] not in seq):
                seq+=s[i]
            else:
                # print("in s[i]")
                ind = max([key for key, value in enumerate(seq) if value == s[i]])
                seq = seq[ind+1:]+s[i]

            # seqs.append(seq)
            if(len(seq)>max_len):
                    max_len = len(seq)
            
        # print(seqs)
        return max_len
                
                

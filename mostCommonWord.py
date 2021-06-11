# 819. Most Common Word

import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if len(paragraph)==0:
            return None
        
        paragraph = (paragraph).lower()
        words = re.split(r"\W+",paragraph)
        if words[-1]=='':
            words = words[:-1]
        
        if(len(words)==0):
            words.append(paragraph)
            
        word_count = {}
        
        # banned = set(banned) Retrieving from list is O(N), while w/ a set it is O(1)
        
        for i in range(len(words)):
            if words[i] not in banned:
                if words[i] not in word_count:
                    word_count[words[i]] = 1
                else:
                    word_count[words[i]]+=1
         
        max_count = 0
        output = ""
        for word, count in (word_count).items():
            if count>max_count:
                max_count = count
                output = word
        
        return output
                
        
        
        

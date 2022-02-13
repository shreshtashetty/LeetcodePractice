# 127. Word Ladder

from collections import defaultdict, deque

# Neetcode's explanation: https://www.youtube.com/watch?v=h9iTnkgv05E

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        #Create adjacency graph
        nei = defaultdict(list)
        wordList.append(beginWord) 
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)
       
        #BFS
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                # Get neighbors of word
                for j in range(len(word)):
                    pattern = word[:j]+"*"+word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res+=1
            
        return 0
        
        
        
                
        
        
        

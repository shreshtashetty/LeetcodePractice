# 290. Word Pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split()

        if(len(words)!=len(pattern)):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        for c, w in zip(pattern, words):
            if c not in char_to_word:
                if w in word_to_char:
                    return False
                else:
                    char_to_word[c] = w
                    word_to_char[w] = c
            else:
                if char_to_word[c]!=w:
                    return False
        return True

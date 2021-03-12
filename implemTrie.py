# 208. Implement Trie (Prefix Tree)

class Node():
    def __init__(self):
        self.children = {}
        self.endofWord = False
        
class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ptr = self.root
        for letter in word:
            if letter not in ptr.children:
                ptr.children[letter] = Node()
            ptr = ptr.children[letter]
        ptr.endofWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ptr = self.root
        for letter in word:
            if letter not in ptr.children:
                return False
            ptr = ptr.children[letter]
        if ptr.endofWord:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ptr = self.root
        for letter in prefix:
            if letter not in ptr.children:
                return False
            ptr = ptr.children[letter]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Node:
    def __init__(self):
        self.child = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root

        for letter in word:
            if letter not in current.child:
                current.child[letter] = Node()
            current = current.child[letter]
        current.end = True

    def search(self, word: str) -> bool:
        current = self.root

        for letter in word:
            if letter in current.child:
                current = current.child[letter]
            else:
                return False
        return current.end

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for letter in prefix:
            if letter in current.child:
                current = current.child[letter]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

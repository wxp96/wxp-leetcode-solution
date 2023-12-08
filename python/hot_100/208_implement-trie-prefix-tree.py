class Trie:

    def __init__(self):
        self.memo=[0]*26
        self.end=False

    def insert(self, word: str) -> None:
        if not word:
            self.end=True
            return
        if not self.memo[ord(word[0])-ord('a')]:
            self.memo[ord(word[0])-ord('a')]=Trie()
        self.memo[ord(word[0])-ord('a')].insert(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return self.end
        if self.memo[ord(word[0])-ord('a')]:
            return self.memo[ord(word[0])-ord('a')].search(word[1:])
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        if self.memo[ord(prefix[0])-ord('a')]:
            return self.memo[ord(prefix[0])-ord('a')].startsWith(prefix[1:])
        else:
            return False

# "Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search","search"
# [],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"]  
tree=Trie()
tree.insert('app')
tree.insert('apple')
tree.search('app')

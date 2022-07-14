class Trie:

    def __init__(self):
        self.children=[None]*26
        self.is_end=False


    def insert(self, word: str) -> None:
        node=self
        for cha in word:
            i=ord(cha)-ord('a')
            if not node.children[i]:
                node.children[i]=Trie()
            node=node.children[i]
        node.is_end=True

    def search_preffix(self,word):
        node=self
        for cha in word:
            i=ord(cha)-ord('a')
            if not node.children[i]:
                return None
            node=node.children[i]
        return node


    def search(self, word: str) -> bool:
        res=self.search_preffix(word)
        if res and res.is_end:
            return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        res=self.search_preffix(prefix)
        return True if res else False

# ["Trie","search"]
# [[],["a"]]

t=Trie()
t.search('a')
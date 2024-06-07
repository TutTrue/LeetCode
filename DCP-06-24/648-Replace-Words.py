class Solution:

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_end_of_word = False
        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, word):
                node = self.root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.is_end_of_word = True

            def starts_with(self, word):
                node = self.root
                tmp = []
                for char in word:
                    if char not in node.children:
                        return word
                    tmp.append(char)
                    node = node.children[char]
                    if node.is_end_of_word:
                        return ''.join(tmp)
                return word
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        res = []
        for i in sentence.split():
            res.append(trie.starts_with(i))

        return ' '.join(res)

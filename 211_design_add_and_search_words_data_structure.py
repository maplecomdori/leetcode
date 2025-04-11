class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def rec(i, node):
            if i == len(word):
                return node.is_end

            char = word[i]
            if char == '.':
                for child in node.children:
                    if rec(i + 1, node.children[child]):
                        return True
                return False

            elif char not in node.children:
                return False
            else:
                return rec(i + 1, node.children[char])

        return rec(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
import typing as t

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children: t.Dict[str, TrieNode] = {}

    def __repr__(self):
        return f'{self.children} -- word: {self.is_word}'
    
    def _collect_suffixes(self, suffix: str, suffixes: list):
        # if found a word, append that suffix
        if self.is_word:
            suffixes.append(suffix)

        # for each node check its children and recurse with added suffix
        for char, node in self.children.items():
            node._collect_suffixes(suffix + char, suffixes)

        return suffixes
    
    def suffixes(self, suffix = '') -> t.List[str]:
        return self._collect_suffixes(suffix, suffixes=[])            
        
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for char in word:
            if char in node.children.keys():
                node = node.children[char]
            else:
                new_node = TrieNode()
                node.children[char] = new_node
                node = new_node

        node.is_word = True

    def exists(self, word: str):
        """
        exists checks if a word exists in trie

        Args:
            word (str): A word
        """
        node = self.root
        for char in word:
            if char in node.children.keys():
                node = node.children[char]
            else:
                return False
        return True
    
    def find(self, prefix: str) -> TrieNode:
        ## Find the Trie node that represents this prefix

        node = self.root
        for char in prefix:
            if char in node.children.keys():
                node = node.children[char]
            else:
                return None
            
        return node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    MyTrie.insert(word)



print("PASS" if MyTrie.find('an').suffixes() == ['t', 'thology', 'tagonist', 'tonym'] else 'FAIL')
print("PASS" if MyTrie.find('ant').suffixes() == ['', 'hology', 'agonist', 'onym'] else 'FAIL')
print("PASS" if MyTrie.find('antag').suffixes() == ['onist'] else 'FAIL')
print("PASS" if MyTrie.find('f').suffixes() == ['un', 'unction', 'actory'] else 'FAIL')

# Edge cases
print("PASS" if MyTrie.find('p') is None else 'FAIL') # doesnt exist
print("PASS" if MyTrie.find('').suffixes() == ["ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"] else 'FAIL') # provided empty prefix


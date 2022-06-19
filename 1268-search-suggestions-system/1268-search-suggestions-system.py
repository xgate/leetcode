class TrieNode:
    def __init__(self):
        self.leaf = False
        self.children = dict()
        
    def insert(self, root, word):
        node = root
        for i in range(len(word)):
            if node.children.get(word[i]):
                node = node.children[word[i]]
            else:
                node.children[word[i]] = TrieNode()
                node = node.children[word[i]]
        node.leaf = True
    
    def search(self, root, word):
        node = root
        prefix = ""
        for i in range(len(word)):
            if node.children.get(word[i]):
                node = node.children[word[i]]
                prefix += word[i]
            else:
                return []        
        result = list()
        self.dfs(node, result, prefix)
        return sorted(result)[:3]
        
    def dfs(self, node, result, word):        
        if not node.children:
            result.append(word)
            return
        if node.leaf:
            result.append(word)
        for k in node.children.keys():
            self.dfs(node.children[k], result, word + k)
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        for p in products:
            root.insert(root, p)
        ans = list()
        for i in range(len(searchWord)):
            ans.append(root.search(root, searchWord[:i+1]))
        return ans

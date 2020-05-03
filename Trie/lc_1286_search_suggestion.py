class TrieNode:
    
    def __init__(self, char):
        
        self.char = char
        self.char_list = [None] * 26
        self.is_word = False


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        """
            Time Space Complexity:
            the length of products array is n, for each word, 
            the length is m 
            Time Complexity: O(n*m)
            Space Compexity: O(n*m)
        """
        
        def build_trie(root, products):

            for product in products:

                current = root

                for char in product:

                    position = ord(char) - ord('a')
                    if current.char_list[position] is None:
                        current.char_list[position] = TrieNode(char)
                    current = current.char_list[position]

                current.is_word = True
                
        def dfs(root, word):
            
            string = ""
            current = root
            for char in word:
                position = ord(char) - ord('a')
                if current.char_list[position] is None:
                    return []
                string += char
                current = current.char_list[position]
            
            stack = [(string, current)]
            matched_words = []
            
            while stack:
                
                string, node = stack.pop()
                if node.is_word:
                    matched_words.append(string)
                
                for next_node in node.char_list:
                    if next_node is not None:
                        stack.append((string + next_node.char, next_node))
            
            # sort the products array
            sorted_words = sorted(matched_words)
            if len(sorted_words) < 3:
                return sorted_words
            return sorted_words[:3]
        
        # build a trie
        root = TrieNode("")
        build_trie(root, products)
        
        # model user input:
        start = 0
        result = []
        for end in range(1, len(searchWord)+1):
            word = searchWord[start: end]
            matched_words = dfs(root, word)
            result.append(matched_words)
        
        return result
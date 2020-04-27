from queue import Queue

class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if not beginWord or not endWord:
            return 0
        
        def create_char_dic():
            char_list = []
            for i in range(26):
                ascii_code = ord("a")
                char_list.append(chr(ascii_code+i))
            return char_list
        
        char_list = create_char_dic()
        q = Queue()
        q.put((beginWord,1))
        visited = set()
        
        def bfs(word_list, level):
            for char in char_list:
                    word_list[i] = char
                    new_word = "".join(word_list)
                    if new_word not in visited and new_word in wordList:
                        visited.add(new_word)
                        q.put((new_word, level+1))
        
        while not q.empty():
            
            word, level = q.get()
            
            if word == endWord:
                return level
            
            word_list = list(word)
            
            for i in range(len(word_list)):
                temp_char = word_list[i]
                bfs(word_list, level)
                word_list[i] = temp_char
                    
        return 0
from queue import Queue

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if not beginWord or not wordList:
            return 0
        
        # Queue
        q = Queue()
        
        # create char list
        def create_char_list():
            char_list = []
            ascii_code = ord("a")
            for i in range(26):
                char_list.append(chr(ascii_code+i))
            return char_list
        
        char_list = create_char_list()
        q.put((beginWord, 1))
        visited = set()
        word_set = set(wordList)
        
        while not q.empty():
            
            word, level = q.get()
            
            if word == endWord:
                return level
            
            word_list = list(word)
            
            for i in range(len(word_list)):
                
                temp_char = word_list[i]
                
                for char in char_list:
                    
                    word_list[i] = char
                    new_word = "".join(word_list)
                    if new_word not in visited and new_word in word_set:
                        visited.add(new_word)
                        q.put((new_word, level + 1))
                        
                word_list[i] = temp_char
            
        return 0

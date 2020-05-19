class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        """
            1. create an order
            2. iterate word by word
            3. iterate letter by letter
            
            Time: O(n * m)
            Space: O(1) 26
        """
        
        def compare(first_word, second_word, dic):
            
            diff = 0
            
            short = min(len(first_word), len(second_word))
            
            for i in range(short):
                if diff == 0:
                    first_char = first_word[i]
                    second_char = second_word[i]
                    diff = dic[first_char] - dic[second_char]

            if diff == 0:
                return len(first_word) - len(second_word)
            else:
                return diff
            
        # create our dictionary
        
        dic = {}
        
        for i in range(len(order)):
            char = order[i]
            dic[char] = i
            
        # iterate word by word, letter by letter
        
        for i in range(1,len(words)):
            prev_word = words[i-1]
            current_word = words[i]
            diff = compare(prev_word, current_word, dic)
            if diff > 0:
                return False
        return True
                
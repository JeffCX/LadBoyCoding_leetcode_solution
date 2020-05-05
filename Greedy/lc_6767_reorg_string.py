from heapq import heappop, heappush

class Solution:
    
    def reorganizeString(self, S: str) -> str:
        
        """
            1. count theh frequency of the char
            2. put the char according to frequency into the max heap
            3. for each iteration,
                get an elment from heap,
                put the char in the result string,
                
                if there is still chars,
                    put it into the temp lst
                    
                append everything from the temp lst back to the heap
                
            Time Complexity: O(n) 
            Space Complexity: O(1)
        """

        #  1. count theh frequency of the char
        dic = {}
        for char in S:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
        print(dic)
        
        #   2. put the char according to frequency into the max heap
        heap = []
        
        for char, frequency in dic.items():
            heappush(heap, (-frequency, char))
            
        result = []

        while heap is not None:
            
            pending_lst = []

            for i in range(2):
                if heap:
                    frequency, char = heappop(heap)
                    positive_frequency = -frequency

                    if positive_frequency > 0:
                        pending_lst.append((positive_frequency-1, char))
                        if result and char == result[-1]:
                            return ""
                        result.append(char)
            
            if not heap and not pending_lst:
                break
            
            for frequency, char in pending_lst:
                heappush(heap, (-frequency, char))

        return "".join(result)
        
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        """
            1. build a hashmap to record the frequenc of each letter
            2. Use heap, use min heap and keep the size as k
            
            Time: O(nlogk)
            Space: O(n)
        """
        
        # 1. build a hashmap to record the frequenc of each letter
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        print(dic)
        
        # top k most frequency words, [1,2], put the frequency into the heap
        heap = []
        for key, frequency in dic.items():
            heappush(heap, (frequency, key))
            if len(heap) > k:
                heappop(heap)
            
        result = []
        for _, element in heap:
            result.append(element)
        return result
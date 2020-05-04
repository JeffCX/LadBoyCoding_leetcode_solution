class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
                                                                                                           
        """
            root:                              [],[2,3]                         1
                                        /                  \
            level 1             [2],[2,3]                   [3],[3]             2
                            /               \             /
            level 2      [2,2],[2,3]      [2,3],[3]      [3,3],[3]              4
                        /           \
            level 3   [2,2,2],[2,3]   [2,2,3],[3]                               8
            
            level n                     1 + 2 + 4 +8 = 2^0 + 2^1 + 2^2 .... = O(2^n)
        """
        
        candidates.sort()
        
        stack = [([], candidates)]
        result = []
        
        while stack:

            state, space = stack.pop()

            if sum(state) == target:
                result.append(state)
            
            if sum(state) < target:
                
                for index in range(len(space)):
                    number = space[index]
                    next_node = state + [number]
                    stack.append((next_node, space[index:]))
                    
        return result
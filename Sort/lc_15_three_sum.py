class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """
            Time: O(n^2)
            Space: O(n)
        
        """
            
        nums.sort()
        target = 0
        
        result = set()
        
        for ind in range(len(nums)):
            
            current = nums[ind]
            goal = target - current
            
            left = ind+1
            right = len(nums) - 1
            while left < right:
                
                left_num = nums[left]
                right_num = nums[right]
                
                if left_num + right_num == goal:
                    result.add((current,left_num,right_num))
                    left += 1
                    right -=1
                    
                elif left_num + right_num > goal:
                    right -= 1
                
                else:
                    left += 1
        
        output = []
        for element in result:
            output.append(element)
        
        return output
    
            
        

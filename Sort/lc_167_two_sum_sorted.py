class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        """
            Time: O(n), 
            Space: O(1)
        """
        
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            
            left_num = numbers[left]
            right_num = numbers[right]
            
            if left_num + right_num == target:
                return [left+1,right+1]
            elif left_num + right_num > target:
                right -= 1
            else:
                left += 1
        
        return []

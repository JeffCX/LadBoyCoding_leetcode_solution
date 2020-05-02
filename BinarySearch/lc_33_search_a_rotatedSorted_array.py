class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """
            O(logn)
        """
        if not nums:
            return -1
        
        # 1. find where it is rotated, find the smallest element
        left = 0
        right = len(nums) - 1
        
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        
        # find which side we need to binary search
        start = left
        left = 0                              
        right = len(nums) - 1  
    
        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start
             
        # standard binary search
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
            
        return -1
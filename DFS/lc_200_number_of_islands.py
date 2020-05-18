class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        """
            Time: O(n * m)
            Space: O(n * m)
        """
        
        if len(grid) == 0:
            return 0
        
        row = len(grid)
        col = len(grid[0])
        
        
        def dfs(grid, r, c):
            
            
            if grid[r][c] == "1":
                
                grid[r][c] = "0"
                
                neighbors = (0,-1), (0,1), (-1,0), (1,0)
                
                for neighbor in neighbors:
                    
                    step_r, step_c = neighbor
                    new_r = r + step_r
                    new_c = c + step_c
                    
                    if  0 <= new_r < row and 0 <= new_c < col:
                        dfs(grid, new_r, new_c)
                    
                    
        num_of_island = 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(grid,r,c)
                    num_of_island += 1
                    
        return num_of_island

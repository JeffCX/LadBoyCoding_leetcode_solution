from copy import deepcopy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        """
             Time: O(n*m)
             Space: O(n*m)
        """
        
        #1. copy the initial state
        init = deepcopy(board)
        rows = len(board)
        cols = len(board[0])
        neighbors = (-1,-1), (-1,0), (-1, 1), (0,-1), (0,1), (1,-1), (1,0), (1,1) 
        
        for r in range(rows):
            for c in range(cols):
                
                live_cell = 0
                dead_cell = 0
                
                for neighbor in neighbors:
                    to_r, to_c = neighbor
                    neighbor_r = r + to_r
                    neigbhor_c = c + to_c
                    
                    if neighbor_r >= 0 and neighbor_r < rows and neigbhor_c >=0 and neigbhor_c < cols:
                        if init[neighbor_r][neigbhor_c] == 0:
                            dead_cell += 1
                        else:
                            live_cell += 1
                    else:
                        dead_cell +=1
                    
                # Any live cell with fewer than two live neighbors dies, as if caused by under-population.
                if init[r][c] == 1 and live_cell < 2:
                    board[r][c] = 0
                    
                # Any live cell with two or three live neighbors lives on to the next generation.
                if init[r][c] == 1 and 2 <= live_cell <= 3:
                    pass
                
                # Any live cell with more than three live neighbors dies, as if by over-population..
                if init[r][c] == 1 and live_cell > 3:
                    board[r][c] = 0
                    
                # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                if init[r][c] == 0 and live_cell == 3:
                    board[r][c] = 1
                
        return board
        
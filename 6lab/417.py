class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
            
        m, n = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(r, c, reachable_set, prev_height):
        
            if (r < 0 or r >= m or c < 0 or c >= n or 
                (r, c) in reachable_set or heights[r][c] < prev_height):
                return
                
    
            reachable_set.add((r, c))
            

            dfs(r + 1, c, reachable_set, heights[r][c])
            dfs(r - 1, c, reachable_set, heights[r][c])
            dfs(r, c + 1, reachable_set, heights[r][c])
            dfs(r, c - 1, reachable_set, heights[r][c])
            
        for r in range(m):
        
            dfs(r, 0, pacific_reachable, heights[r][0])
            
            dfs(r, n - 1, atlantic_reachable, heights[r][n - 1])
                  
        for c in range(n):
            
            dfs(0, c, pacific_reachable, heights[0][c])
            
            dfs(m - 1, c, atlantic_reachable, heights[m - 1][c])
            
        return [list(cell) for cell in pacific_reachable.intersection(atlantic_reachable)]
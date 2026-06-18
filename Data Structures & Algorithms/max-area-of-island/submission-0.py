class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row,col = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = self.calculate_area(grid,row, col, visited, i, j)
                    max_area = max(max_area, area)
        
        return max_area

    
    def calculate_area(self, grid, row,col, visited, cr, cc):
        if cr < 0 or cr >= row or cc < 0 or cc >=col or (cr,cc) in visited or grid[cr][cc] == 0:
            return 0
        visited.add((cr,cc))
        return (1 + self.calculate_area(grid, row,col,visited, cr+1,cc) +
            self.calculate_area(grid, row,col,visited, cr-1,cc) +
            self.calculate_area(grid, row,col,visited, cr,cc+1) +
            self.calculate_area(grid, row,col,visited, cr,cc-1))
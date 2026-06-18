class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        visited = set()
        island = 0


        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i,j) not in visited:
                    island +=1
                    self.dfs(grid,row,col,visited,i,j)
        return island

    def dfs(self, grid, r, c, visited, cr, cc):
        if cr < 0 or cr >=r or cc<0 or cc >=c or (cr,cc) in visited or grid[cr][cc] =='0':
            return

        visited.add((cr,cc))
        self.dfs(grid, r,c, visited, cr-1, cc)
        self.dfs(grid, r,c,visited, cr+1, cc)
        self.dfs(grid, r, c, visited, cr, cc+1)
        self.dfs(grid, r,c, visited, cr, cc-1)
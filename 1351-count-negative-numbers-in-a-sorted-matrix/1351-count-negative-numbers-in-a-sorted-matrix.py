class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return len([grid[i][j] for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j]<0])
        
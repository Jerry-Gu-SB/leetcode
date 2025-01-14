class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # this is kind of like a flood fill paint bucket type thing

        rows, cols = len(grid), len(grid[0])

        # linear search through the 2d array
        # if encounter 1, increment solution counter
        #   then BFS to get every single piece of land
        #   mark every piece of land with a third data point (-1 for us)
        # if encounter 0 or -1, skip
        # return solution counter

        # bug, how to change list while iterating through it?
        # just iterate through the range lens and it shoudl be ok

        visited = set()

        def bfs(r, c):
            stack = [(r, c)]
            visited.add((r, c))

            while stack:
                row, col = stack.pop(0)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited:
                        stack.append((r, c))
                        visited.add((r, c))

        solution = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    solution += 1
                    bfs(r, c)

        return solution


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[len(grid) - 1][len(grid) - 1] == 1:
            return -1
        direction_list = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        # just a dfs or bfs innit. you could even do an A* i think

        queue = deque([[0, 0, 1]])
        visited = [[False] * len(grid) for _ in range(len(grid))]
        visited[0][0] == True
        paths = []
        while queue:
            cur_x, cur_y, cur_len = queue.popleft()
            # print("-------------------------------queue:", queue)
            # print("cur_x, cur_y", cur_x, cur_y)
            # print("visited:", visited)
            if cur_x == len(grid) - 1 and cur_y == len(grid) - 1:
                return cur_len

            for x, y in direction_list:
                new_x = cur_x + x
                new_y = cur_y + y
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid) and not visited[cur_x][cur_y] and grid[new_x][new_y] == 0:
                    queue.append([new_x, new_y, cur_len + 1])
            visited[cur_x][cur_y] = True
        return -1

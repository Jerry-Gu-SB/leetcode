class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # linearly iterate through teh board
        # if the first letter exists, then DFS to find the rest of the word

        # directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        # m = len(board)
        # n = len(board[0])

        # def dfs(i, j):
        #     print("------dfs call-------")
        #     stack = [(i, j, 1)]
        #     visited = [[False] * n for _ in range(m)]

        #     while stack:
        #         cur_x, cur_y, cur_index = stack.pop(-1)
        #         print("cur_index:", cur_index)
        #         print("cur position:", "[", cur_x, cur_y, "]")
        #         print("stack:", stack)
        #         if cur_index == len(word):
        #             return True

        #         for x, y in directions:
        #             new_x, new_y = cur_x + x, cur_y + y

        #             # print("new coor:","[", new_x, new_y, "]")

        #             if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y] and board[new_x][new_y] == word[cur_index]:
        #                 print("visited[new_x][new_y]:", visited[new_x][new_y])
        #                 print("board[new_x][new_y]:", board[new_x][new_y])
        #                 print("word[cur_index]:", word[cur_index])
        #                 stack.append((new_x, new_y, cur_index + 1))
        #             visited[cur_x][cur_y] = True
        #     return False

        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == word[0]:
        #             if dfs(i, j):
        #                 return True
        # return False

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        m = len(board)
        n = len(board[0])
        path = set()

        def dfs(cur_x, cur_y, cur_index):
            if cur_index == len(word):
                return True
            if (not (0 <= cur_x < m)) or (not (0 <= cur_y < n)) or ((cur_x, cur_y) in path) or (
                    board[cur_x][cur_y] != word[cur_index]):
                return False

            res = False
            path.add((cur_x, cur_y))
            for x, y in directions:
                new_x, new_y = cur_x + x, cur_y + y
                res = res or dfs(new_x, new_y, cur_index + 1)
            path.remove((cur_x, cur_y))
            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
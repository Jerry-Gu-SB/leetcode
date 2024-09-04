class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # brute force: bfs every single cell until you find a zero and then count the layer
        # keep the x and y coordinates the same and in order until you actually access them inside a matrix. then just flip ONLY when indexing into mat

        # create adjacency list
        adj = {}
        max_y = len(mat)
        max_x = len(mat[0])

        sol = [[0 for x in range(len(mat[0]))] for y in range(len(mat))]

        for y in range(len(mat)):
            for x in range(len(mat[0])):
                paths = set()
                if y > 0:
                    paths.add((x, y - 1))
                if y < max_y:
                    paths.add((x, y + 1))
                if x > 0:
                    paths.add((x - 1, y))
                if x < max_x:
                    paths.add((x + 1, y))
                adj[x, y] = paths

        # bfs
        def bfs(layer, cur, queue, visited):
            visited.add(cur)

            for path in adj[cur]:
                if path not in visited:
                    queue.append(path)

            while queue:

        return bfs(0, (0, 0), [], set())


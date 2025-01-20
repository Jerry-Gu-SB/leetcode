class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # this is pretty nuts problem
        # I think the key here is that the dictionary is really small, so i think you can just do a linear search through the dictionary over and over again is my intuition
        # kind of feels liek we can just take the first word, we find, then breka the problem down into "word" + subproblem

        # I"m getting kind of a DP sort of angle here

        # The problem is with a case of "applepen", you need to get the "pen" segment after you see "apple"

        # i think you need to iterate through the string at every single character, grab every word that corresponds to the dictionary (and this is actually okay because the strong is max 20 characters, so it's constant time)
        # Then at every word at every character, you can then subdivide the problem
        # you can represent this with a max 20 node graph, and connect each node to the end
        # then you just connect each index to the next index of the next word that exists in the sentence
        # then you reduce the problem to finding every single path to the end.
        #   DFS to create the output

        # step 1: create the graph! (adjacency list)
        END_VERTEX = -21

        def get_vertex(index):
            indices = []
            sub_str = s[index:]
            for i in range(len(sub_str)):
                if sub_str[:i] in wordDict:
                    indices.append(i + index)
                    # if len(sub_str[:i]) + index + i == len(s):  # check whether we've reached the end of the string
                    #     indices.append(END_VERTEX)
            return indices

        graph = {}
        graph[END_VERTEX] = []

        for i in range(len(s)):
            graph[i] = get_vertex(i)
        graph[END_VERTEX] = []
        print(graph)
        for i in range(len(s)):
            if s[i:] in wordDict:
                graph[i].append(END_VERTEX)
        print(graph)

        # step 2: take graph, run DFS on it!
        # WAIT, the problem with this, is that there can be an extra letter at the end unaccounted for.

        # STUDY THIS
        def find_all_paths(graph, start, end, path=[]):
            path = path + [start]
            if start == end:
                return [path]
            if start not in graph.keys():
                return []

            paths = []
            for node in graph[start]:
                if node not in path:
                    newpaths = find_all_paths(graph, node, end, path)
                    for newpath in newpaths:
                        paths.append(newpath)
            return paths

        path_list = find_all_paths(graph, 0, END_VERTEX)

        print(path_list)

        # step 3: take the paths, insert the spaces
        solution = []
        for path in path_list:
            print("cur_path:", path)
            cur_list = []
            cur_word = ""
            for i, char in enumerate(s):
                print("i:", i, "cur_word:", cur_word)

                if i in path and (i != 0 and i != END_VERTEX):
                    print("PUTTING IN THIS WORD:", cur_word)
                    cur_list.append(cur_word)
                    cur_word = char
                else:
                    cur_word += char
            cur_list.append(cur_word)
            print("cur list:", cur_list)
            solution.append(cur_list)

        actual_solution = []
        for listo in solution:
            stringo = ""
            for i, wordo in enumerate(listo):
                stringo += wordo
                if i != len(listo) - 1:
                    stringo += " "
            actual_solution.append(stringo)
        return actual_solution

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict,deque
        que = deque()
        adj_list = defaultdict(list)
        visited = defaultdict(list)
        for ele1, ele2 in edges:
            adj_list[ele1].append(ele2)
            adj_list[ele2].append(ele1)
        for nodes in range(n):
            visited[nodes]=0

        no_of_islands = 0
        visited_copy = visited.copy()
        for node, visit in visited.items():
            if visited_copy[node]==1:
                continue
            no_of_islands+=1
            que.append(node)
            visited_copy[node]=1
            while que:
                node = que.popleft()
                for neighbours in adj_list[node]:
                    if visited_copy[neighbours]==0:
                        visited_copy[neighbours]=1
                        que.append(neighbours)
        return no_of_islands




            

        
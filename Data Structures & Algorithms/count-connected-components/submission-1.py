class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict,deque
        adj_list = defaultdict(list)
        visited = defaultdict(int)
        for i in range(0,n):
            visited[i]=0
        for ele in edges:
            adj_list[ele[0]].append(ele[1])
            adj_list[ele[1]].append(ele[0])
        connected_components = 0
        for node in visited.keys():
            if visited[node]==1:
                continue
            connected_components+=1
            que = deque()
            que.append(node)
            visited[node]=1
            while que:
                node = que.popleft()
                for node_neighbours in adj_list[node]:
                    if visited[node_neighbours]==0:
                        visited[node_neighbours]=1
                        que.append(node_neighbours)
        return connected_components


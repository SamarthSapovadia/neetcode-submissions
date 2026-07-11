class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import defaultdict,deque
        adj_list = defaultdict(list)
        visited = defaultdict()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                node = (row,col)
                if grid[row][col]=="0":
                    continue
                visited[node]=0
                for movement in [(1,0),(-1,0),(0,1),(0,-1)]:
                    dx = row+movement[0]
                    dy = col + movement[1]
                    
                    if ((dx>=0 and dx<len(grid)) and (dy>=0 and dy <len(grid[0]))):
                        if grid[dx][dy]=="1":
                            adj_list[node].append((dx,dy))
        island = 0
        print(adj_list)
        for keys in visited.keys():
            if visited[keys]==1:
                continue
            island+=1
            visited[keys]=1
            que = deque()
            que.append(keys)
            while que:
                node = que.popleft()
                for neigbhours_node in adj_list[node]:
                    if visited[neigbhours_node]==0:
                        visited[neigbhours_node]=1
                        que.append(neigbhours_node)
        return island

            


        
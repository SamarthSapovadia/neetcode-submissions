class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import defaultdict,deque
        adj_list = defaultdict(list)
        visited = defaultdict()
        que = deque()
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                node = (row,col)
                if grid[row][col] in [-1]:
                    continue
                if grid[row][col]==0:
                    que.append((node,0))
                visited[node]=0
                for movement in [[1,0],[-1,0],[0,-1],[0,1]]:
                    dx = row+movement[0]
                    dy = col + movement[1]
                    if (dx>=0 and dx <len(grid)) and (dy >=0 and dy <len(grid[0])):
                        if grid[dx][dy] !=-1:
                            visited[(dx,dy)]=0
                            adj_list[node].append((dx,dy))   
        
        while que:
            node,dist = que.popleft()
            for neighbours in adj_list[node]:
                if visited[neighbours] !=1:
                    visited[neighbours]=1
                    que.append((neighbours,dist+1))
                    if grid[neighbours[0]][neighbours[1]]>2:
                        grid[neighbours[0]][neighbours[1]]=dist+1
                    


        


        
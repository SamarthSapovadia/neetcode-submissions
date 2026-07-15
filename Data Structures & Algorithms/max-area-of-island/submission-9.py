class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from collections import defaultdict,deque
        adj_list = defaultdict(list)
        visited = defaultdict(int)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==0:
                    continue
                node = (row,col)
                visited[node]=0
                for movement in [[0,1],[0,-1],[1,0],[-1,0]]:
                    dx = row + movement[0]
                    dy = col + movement[1]
                    if (dx>=0 and dx<len(grid)) and (dy>=0 and dy <len(grid[0])):
                        if grid[dx][dy]==1:
                            adj_list[node].append((dx,dy))
        if len(adj_list)==0 and len(visited)==0:
            return 0
            
        max_area = 1                
        for node,visited_flag in visited.items():
            if visited_flag==1:
                continue
            visited[node]=1
            stack = []
            stack.append((node,1))
            temp = 1
            while stack:
                # print(stack)
                node,dist = stack.pop()
                for neigbhour_node in adj_list[node]:
                    if visited[neigbhour_node] !=1:
                        visited[neigbhour_node]=1
                        temp+=1
                        stack.append((neigbhour_node,dist))
                        if temp > max_area:
                            max_area = temp
        return max_area







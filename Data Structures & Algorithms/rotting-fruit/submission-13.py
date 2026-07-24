class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        from collections import deque
        adj_list = defaultdict(list)
        visited = defaultdict(int)
        rotten_oranges = deque()
        non_rotten_oranges = defaultdict(int)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                node = (row,col)
                if grid[row][col]==1:
                    non_rotten_oranges[node]=0
                if grid[row][col]==2:
                    rotten_oranges.append((node,0))
                for movement in ([1,0],[-1,0],[0,1],[0,-1]):
                    dx = row + movement[0]
                    dy = col + movement[1]
                    if (dx>=0 and dx< len(grid)) and (dy >=0 and dy < len(grid[0])):
                        if grid[dx][dy] !=0:
                            adj_list[node].append((dx,dy))
        max_time = -1
        if len(non_rotten_oranges)==0:
            return 0
        while rotten_oranges:
            print(rotten_oranges)
            node,time = rotten_oranges.popleft()
            print(node,time,max_time)
            for neighbours in adj_list[node]:
                if time > max_time:
                    max_time = time
                if neighbours in non_rotten_oranges:
                    rotten_oranges.append((neighbours,time+1))
                    non_rotten_oranges.pop(neighbours)
        if len(non_rotten_oranges)>0:
            return -1
        return max_time





        
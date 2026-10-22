class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import defaultdict,deque
        adj_list = defaultdict(list)
        rotten_oranges = deque()
        non_rotten = defaultdict()
        for col in range(len(grid[0])):
            for row in range(len(grid)):
                if grid[row][col]==0:
                    continue
                else:
                    if grid[row][col]==2:
                        rotten_oranges.append(((row,col),0))
                    else:
                        non_rotten[(row,col)]=0

                    for movement in [[1,0],[0,1],[-1,0],[0,-1]]:
                        dx = movement[0] + row
                        dy = movement[1] + col
                        if ((dx>=0 and dx < len(grid))& (dy>=0 and dy < len(grid[0]))):
                            adj_list[(row,col)].append((dx,dy))
        max_time = 0
        while rotten_oranges:
            node,time = rotten_oranges.popleft()
            print(rotten_oranges)
            if max_time<time:
                max_time = time
            for neighbours in adj_list[node]:
                if ((grid[neighbours[0]][neighbours[1]]==1) and (non_rotten[neighbours]==0)) :
                    non_rotten[neighbours]=1
                    rotten_oranges.append((neighbours,time+1))
        for values in non_rotten.values():
            if values==0:
                return -1
        return max_time




                        
                        





        
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import defaultdict ,deque
        que = deque()
        visited_node = defaultdict()
        non_rotten = set()
        max_time = 0
        dict_ = defaultdict(list)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                node = (row,col)
                if grid[row][col]==2:
                    que.append((node,0))
                if grid[row][col]==1:
                    non_rotten.add((row,col))
                for movement in [[0,1],[0,-1],[1,0],[-1,0]]:
                    dx = row+movement[0]
                    dy = col + movement[1]
                    if ((dx>=0 and dx <len(grid)) and (dy>=0 and dy <len(grid[0])) and (grid[dx][dy]==1)):
                        
                        dict_[node].append((dx,dy))
        # print(dict_,que)
        while que:
            node,time = que.popleft()
            if time >= max_time:
                max_time = time
            for neighbours in dict_[node]:
                if grid[neighbours[0]][neighbours[1]]==1:
                    que.append((neighbours,time+1))
                    grid[neighbours[0]][neighbours[1]] = 2
                    non_rotten.remove(neighbours)
        print(non_rotten)
        if len(non_rotten) >0:
            return -1
        return max_time



                    







        
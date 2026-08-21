class Solution:
    def solve(self, board: List[List[str]]) -> None:
        from collections import defaultdict,deque
        que =  deque()
        neighbours = defaultdict(list)
        visited = defaultdict(int)
        for row in range(len(board)):
            for col in range(len(board[0])):
                ele = board[row][col]
                if ele =='X':
                    continue
                else:                   
                    visited[(row,col)]=0    
                    if ((row==len(board)-1) or (col==len(board[0])-1)) or ((row==0) or (col==0)) :
                        que.append((row,col))
                        visited[(row,col)]=1
                    for movement in ([1,0],[-1,0],[0,1],[0,-1]):
                        dx = row + movement[0]
                        dy = col + movement[1]
                        if ((dx>=0 and  dx <len(board)) and (dy>=0 and dy <len(board[0])) and (board[dx][dy]=='O')):
                            neighbours[(row,col)].append((dx,dy))
        

        while que:
            node = que.pop()
            for neigbhour in neighbours[node]:
                if visited[neigbhour]==0:
                    visited[neigbhour] = 1
                    que.append(neigbhour)
        for ele,check in visited.items():
            if check ==1:
                continue
            else:
                board[ele[0]][ele[1]]='X'

        


                    



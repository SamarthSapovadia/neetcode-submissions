class Solution:
    def pos(self,p,matrix):
        return ((p//len(matrix[0])), p - (p//len(matrix[0]))*len(matrix[0]))
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        p1 = 0
        p2 = len(matrix)*len(matrix[0])-1
        while p2>=p1:
            mid = (p2+p1)//2
            mid_pos = self.pos(mid,matrix)
            print(mid_pos,mid)
            print(matrix[mid_pos[0]][mid_pos[1]])
            if target ==matrix[mid_pos[0]][mid_pos[1]]:
                return True
            elif target > matrix[mid_pos[0]][mid_pos[1]]:
                print('yes')
                p1 = mid+1
                p2 =p2
            elif target < matrix[mid_pos[0]][mid_pos[1]]:
                p1 = p1
                p2 = mid-1
        return False




        
        
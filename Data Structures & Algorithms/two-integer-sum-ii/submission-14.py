class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = len(numbers)-1
        index2 = 0
        while index1 != index2:
            total = numbers[index1]+numbers[index2]
            if total == target:
                return [index2+1,index1+1]
            elif total > target:
                index1-=1
            elif total < target:
                index2+=1
        return []







        
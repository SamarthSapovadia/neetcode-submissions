class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers)<1:
            return []
        for index1 in range(0,len(numbers)):
            for index2 in range(index1+1,len(numbers)):
                total = numbers[index1]+numbers[index2]
                if total==target:
                    return [index1+1,index2+1]
        return []
        
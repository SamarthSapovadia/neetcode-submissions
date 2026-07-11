class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers)<1:
            return []
        if len(numbers)==2:
            if target == (numbers[0]+numbers[1]):
                return [1,2]
            else:
                return []
        index1 = 0
        index2 = 1
        while (index1 != 0 or index2 != len(numbers)-1):
            total  = numbers[index1] + numbers[index2]
            print(index1,index2,total)
            if total ==target:
                return [index1+1,index2+1]
            elif (total > target) and (index1 !=0):
                index1 -=1
            elif (total < target) and (index2 != len(numbers)-1):
                index1+=1
                index2+=1
            if index2 == len(numbers)-1 and index1 == 0:
                total  = numbers[index1] + numbers[index2]
                if total == target:
                    return [index1+1,index2+1]
                else:
                    return []





        
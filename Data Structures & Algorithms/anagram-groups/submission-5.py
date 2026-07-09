class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict
        dict_ = defaultdict(int)
        dict_map = defaultdict(list)

        import string

        pos=0
        for char in string.ascii_lowercase:
            dict_[char]=pos
            pos+=1
        
        for ele in strs:
            arr = [0]*27
            sum=0
            for char in ele:
                sum+=ord(char)
                arr[dict_[char]]=1
            arr[26]=sum
            dict_map[tuple(arr)].append(ele)
        arr = []
        for key,value in dict_map.items():
            arr.append(value)
        return arr

            




        
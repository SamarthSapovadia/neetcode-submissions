class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        s1 = defaultdict(int)
        s2 = defaultdict(int)
        for ele in s:
            s1[ele]+=1
        for ele in t:
            s2[ele]+=1
        loop_dict = s1 if len(s1)>= len(s2) else s2 
        for key,value in loop_dict.items():
            if key in s2:
                if s2[key]==s1[key]:
                    continue
                else:
                    return False
            else:
                return False
        return True
        
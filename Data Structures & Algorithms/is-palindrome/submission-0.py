class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string

        alphanumeric_chars = string.ascii_letters + string.digits
        s = s.lower()
        print(s)
        dict_map = {}
        pos = 0
        for char in alphanumeric_chars:
            dict_map[char]=pos
            pos+=1
        str_list = s.split(' ')
        full_str = ''
        for ele in str_list:
            for char in ele:
                if char in dict_map:
                    full_str+=char
        for pos in range(0,len(full_str)//2):
            if full_str[pos] != full_str[len(full_str)-pos-1]:
                return False
        return True





        







                
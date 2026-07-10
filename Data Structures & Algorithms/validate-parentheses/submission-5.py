class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = set(['[','{','('])
        for ele in s:
            if ele in check :
                stack.append(ele)
            else:
                if len(stack)==0:
                    return False
                pop_ele = stack.pop()
                if ele ==']' and pop_ele != '[':
                    return False
                elif ele ==')' and pop_ele != '(':
                    return False
                elif ele =='}' and pop_ele != '{':
                    return False
        return True if len(stack)==0 else False


        
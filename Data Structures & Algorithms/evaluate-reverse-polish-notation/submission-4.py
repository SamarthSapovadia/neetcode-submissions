class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import math
        stack = []
        for char in tokens:
            if char == "+":
                number  = stack.pop() + stack.pop()
                stack.append(number)
            elif char == "*":
                number  = stack.pop()*stack.pop()
                stack.append(number)
            elif char == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                number  = num2 - num1
                stack.append(number)
            elif char == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                number  = num2/num1
                if number>0:
                    number = math.floor(number)
                else:
                    number = math.ceil(number)


                stack.append(number)
            else:
                stack.append(int(char))
            print(stack)
        return stack[0]
        (((10 * (6 / ((9 + 3) * -11))) + 17) + 5)





            
        